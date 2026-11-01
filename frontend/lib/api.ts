import { PortfolioPosition, UploadResponse, RunResponse } from "./types";

const getBaseUrl = (): string => {
  if (process.env.NEXT_PUBLIC_API_URL) {
    return process.env.NEXT_PUBLIC_API_URL;
  }
  if (typeof window !== "undefined") {
    const host = window.location.hostname || "localhost";
    return `${window.location.protocol}//${host}:8000/api`;
  }
  return "http://127.0.0.1:8000/api";
};

const BASE = getBaseUrl();

export async function uploadPdf(file: File): Promise<UploadResponse> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${BASE}/upload-pdf`, { method: "POST", body: form });
  if (!res.ok) throw new Error(`Upload failed: ${res.statusText}`);
  const data: UploadResponse = await res.json();

  // Surface extraction failures on the upload page rather than silently
  // navigating to a run with zero positions.
  if (data.extraction_status === "failed" || data.extraction_status === "partial") {
    throw new Error(data.extraction_message);
  }

  return data;
}

export async function loadSamplePortfolio(): Promise<UploadResponse> {
  const res = await fetch(`${BASE}/sample-portfolio`);
  if (!res.ok) throw new Error(`Sample load failed: ${res.statusText}`);
  return res.json();
}

export async function startRun(
  runId: string,
  positions: PortfolioPosition[],
  maxRetries = 2
): Promise<RunResponse> {
  const res = await fetch(`${BASE}/run`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ run_id: runId, positions, max_retries: maxRetries }),
  });
  if (!res.ok) throw new Error(`Run failed: ${res.statusText}`);
  return res.json();
}

export function getStreamUrl(runId: string): string {
  return `${BASE}/stream/${runId}`;
}

export async function exportRunJson(runId: string): Promise<unknown> {
  const res = await fetch(`${BASE}/result/${runId}`);
  if (!res.ok) throw new Error(`Export failed: ${res.statusText}`);
  return res.json();
}
