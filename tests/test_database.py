import sys
import sqlite3
from datetime import datetime
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from analytics import summarize_detections
from database import init_db, log_detection


def test_audit_log_persists_detection_results_and_analytics(tmp_path):
    db_path = tmp_path / "nested" / "audit.db"
    init_db(db_path)
    log_detection("sample-present.jpg", True, 0.9, "ALLOW: accepted", db_path)
    log_detection("sample-unclear.jpg", False, 0.4, "REVIEW: verify", db_path)
    log_detection("sample-unavailable.jpg", None, None, "REVIEW: unavailable", db_path)

    summary = summarize_detections(db_path)

    assert summary["total_events"] == 3
    assert summary["detection_counts"] == {
        "detected": 1,
        "not_detected": 1,
        "unavailable": 1,
    }
    assert summary["decision_counts"] == {"ALLOW": 1, "REVIEW": 2}
    assert summary["mean_confidence"] == pytest.approx(0.65)
    assert sum(summary["daily_counts"].values()) == 3


def test_audit_log_records_utc_timestamp(tmp_path):
    db_path = tmp_path / "audit.db"
    init_db(db_path)
    log_detection("sample.jpg", True, 0.9, "ALLOW: accepted", db_path)

    with sqlite3.connect(db_path) as connection:
        created_at = connection.execute(
            "SELECT created_at FROM detections"
        ).fetchone()[0]

    timestamp = datetime.fromisoformat(created_at)
    assert timestamp.utcoffset().total_seconds() == 0


@pytest.mark.parametrize("confidence", [-0.1, 1.1, float("nan"), float("inf")])
def test_audit_log_rejects_invalid_confidence(tmp_path, confidence):
    db_path = tmp_path / "audit.db"
    init_db(db_path)
    with pytest.raises(ValueError, match="confidence"):
        log_detection("sample.jpg", True, confidence, "ALLOW", db_path)


def test_audit_summary_handles_empty_database(tmp_path):
    db_path = tmp_path / "audit.db"
    init_db(db_path)

    assert summarize_detections(db_path) == {
        "total_events": 0,
        "detection_counts": {},
        "decision_counts": {},
        "mean_confidence": None,
        "daily_counts": {},
    }


@pytest.mark.parametrize(
    ("id_detected", "confidence"),
    [(True, None), (False, None), (None, 0.5)],
)
def test_audit_log_rejects_inconsistent_detection_values(
    tmp_path, id_detected, confidence
):
    db_path = tmp_path / "audit.db"
    init_db(db_path)
    with pytest.raises(ValueError, match="confidence"):
        log_detection("sample.jpg", id_detected, confidence, "REVIEW", db_path)
