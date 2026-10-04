# Audit data dictionary

The SQLite audit log is an append-only record of the demo workflow. It contains synthetic scenarios and is not evidence of real ID verification.

| Field | Type | Meaning |
|-------|------|---------|
| `id` | Integer | Database-generated event identifier. |
| `image_path` | Text | Input label or path associated with the event. The demo uses synthetic sample names; avoid storing real ID images or personally identifying paths. |
| `id_detected` | Integer / null | `1` means the simulated detector reported an ID, `0` means it did not, and `NULL` means detection was unavailable. |
| `confidence` | Real / null | Detector confidence on the inclusive `[0, 1]` scale; `NULL` when detection is unavailable. This prototype score is not calibrated. |
| `decision` | Text | Rule-engine outcome (`ALLOW`, `WARNING`, or `REVIEW`) and its explanation. Missing, weak, or unavailable detection always requires manual review. |
| `created_at` | ISO 8601 text | Event timestamp with UTC offset. |

## Summary metrics

`summarize_detections()` returns total events, detection and decision counts, mean confidence over events with a score, and counts grouped by the UTC date in `created_at`. The mean is descriptive only: it does not measure model quality, calibration, or accuracy. Evaluate those metrics against labeled data before integrating a real detector.

The default database is `data/detections.db`. Set `ID_DETECTION_DB_PATH` to direct the app elsewhere. The demo appends records on every run.
