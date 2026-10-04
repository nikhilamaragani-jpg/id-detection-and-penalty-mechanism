"""SQLite persistence for ID detection decisions."""

from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime, timezone
import os
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "detections.db"


def _database_path(db_path: str | os.PathLike | None = None) -> Path:
    configured_path = db_path or os.environ.get("ID_DETECTION_DB_PATH") or DB_PATH
    return Path(configured_path).expanduser()


@contextmanager
def connect_database(
    db_path: str | os.PathLike | None = None,
) -> Iterator[sqlite3.Connection]:
    """Yield a transactional SQLite connection and close it after use."""
    path = _database_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=5)
    connection.row_factory = sqlite3.Row
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def init_db(db_path: str | os.PathLike | None = None) -> None:
    """Create the audit table and query indexes if they do not exist."""
    with connect_database(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT NOT NULL,
                id_detected INTEGER CHECK (id_detected IN (0, 1) OR id_detected IS NULL),
                confidence REAL CHECK (confidence BETWEEN 0 AND 1 OR confidence IS NULL),
                decision TEXT NOT NULL,
                created_at TEXT NOT NULL,
                CHECK (
                    (id_detected IS NULL AND confidence IS NULL) OR
                    (id_detected IS NOT NULL AND confidence IS NOT NULL)
                )
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_detections_created_at "
            "ON detections (created_at)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_detections_decision "
            "ON detections (decision)"
        )


def log_detection(
    image_path: str,
    id_detected: bool | None,
    confidence: float | None,
    decision: str,
    db_path: str | os.PathLike | None = None,
) -> None:
    """Append one decision to the audit log."""
    if not isinstance(image_path, str) or not image_path.strip():
        raise ValueError("image_path must be a non-empty string")
    if id_detected is not None and not isinstance(id_detected, bool):
        raise TypeError("id_detected must be True, False, or None")
    if (id_detected is None) != (confidence is None):
        raise ValueError("confidence must be None only when detection is unavailable")
    if confidence is not None:
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
            raise TypeError("confidence must be a number or None")
        if not 0 <= confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
    if not isinstance(decision, str) or not decision.strip():
        raise ValueError("decision must be a non-empty string")

    with connect_database(db_path) as connection:
        connection.execute(
            """
            INSERT INTO detections (image_path, id_detected, confidence, decision, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                image_path,
                None if id_detected is None else int(id_detected),
                confidence,
                decision,
                datetime.now(timezone.utc).isoformat(),
            ),
        )
