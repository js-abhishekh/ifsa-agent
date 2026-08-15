#!/bin/bash
# Start both FastAPI backend and Next.js frontend

echo "=== Starting IFSA's FRTB-SA Auditor ==="

# Start FastAPI backend on port 8000
cd /app
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Start Next.js frontend on port 3000
cd /app/frontend
npm start &
FRONTEND_PID=$!

echo "=== Backend PID: $BACKEND_PID, Frontend PID: $FRONTEND_PID ==="
echo "=== Frontend: http://localhost:3000 ==="
echo "=== Backend:  http://localhost:8000 ==="

# Terminate both if either is killed
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null" EXIT

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
exit $?
