"""Aggregate audit events into a compact operational summary."""

import sqlite3
from collections import Counter
from pathlib import Path

from database import connect_database


def summarize_detections(db_path: str | Path | None = None) -> dict:
    """Return detection, decision, confidence, and daily-volume metrics."""
    with connect_database(db_path) as connection:
        rows = connection.execute(
            """
            SELECT id_detected, confidence, decision, substr(created_at, 1, 10) AS day
            FROM detections
            ORDER BY created_at, id
            """
        ).fetchall()

    detection_counts = Counter()
    decision_counts = Counter()
    daily_counts = Counter()
    confidences = []

    for row in rows:
        if row["id_detected"] is None:
            detection_counts["unavailable"] += 1
        elif row["id_detected"]:
            detection_counts["detected"] += 1
        else:
            detection_counts["not_detected"] += 1

        decision_counts[row["decision"].split(":", 1)[0]] += 1
        daily_counts[row["day"]] += 1
        if row["confidence"] is not None:
            confidences.append(row["confidence"])

    return {
        "total_events": len(rows),
        "detection_counts": dict(sorted(detection_counts.items())),
        "decision_counts": dict(sorted(decision_counts.items())),
        "mean_confidence": (
            sum(confidences) / len(confidences) if confidences else None
        ),
        "daily_counts": dict(sorted(daily_counts.items())),
    }
