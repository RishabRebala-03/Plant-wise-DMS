export function formatDetailedTimestamp(value?: string | null, fallback = "-") {
  if (!value) return fallback;
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) return value;
  return parsed.toLocaleString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
    timeZoneName: "short",
  });
}

export function getDocumentTimestamp(value?: { uploadedAt?: string | null; date?: string | null }, fallback = "-") {
  return formatDetailedTimestamp(value?.uploadedAt ?? value?.date, fallback);
}
