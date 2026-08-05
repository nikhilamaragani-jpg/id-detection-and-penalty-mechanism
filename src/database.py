"""
SQLite logging for ID detection decisions
"""

import sqlite3
import os
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "data", "detections.db")


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            id_detected INTEGER,
            confidence REAL,
            decision TEXT,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def log_detection(image_path: str, id_detected: bool, confidence: float, decision: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO detections (image_path, id_detected, confidence, decision, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            image_path,
            int(id_detected),
            confidence,
            decision,
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    conn.commit()
    conn.close()
