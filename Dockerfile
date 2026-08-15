# ── Stage 1: Build Next.js frontend for IFSA's FRTB-SA Auditor ──────────────────
FROM node:20-slim AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ .
RUN npm run build

# ── Stage 2: Python runtime with all deps ────────────────────────────────────
FROM python:3.11-slim AS final

# Install Node.js for Next.js production server
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies (root + backend)
COPY requirements.txt ./
COPY backend/requirements.txt ./backend-requirements.txt
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt -r backend-requirements.txt

# HF Token for authenticated, fast downloads
ENV HF_TOKEN=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

# Copy Python source code
COPY src/ ./src/
COPY backend/ ./backend/
COPY data/ ./data/
COPY run_pipeline.py .

# Copy built Next.js app
COPY --from=frontend-builder /app/frontend/.next ./frontend/.next
COPY --from=frontend-builder /app/frontend/public ./frontend/public
COPY --from=frontend-builder /app/frontend/node_modules ./frontend/node_modules
COPY --from=frontend-builder /app/frontend/package.json ./frontend/package.json

# Create uploads directory
RUN mkdir -p data/uploads

# Copy startup script
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 3000 8000

CMD ["./start.sh"]
