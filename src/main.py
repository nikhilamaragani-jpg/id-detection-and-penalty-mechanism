"""
ID Card Detection and Penalty Mechanism
Prototype with detection rules + SQLite logging
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from detector import basic_image_check
from rules import apply_penalty_rule
from database import init_db, log_detection


def main():
    print("=" * 55)
    print("ID Detection & Penalty Mechanism - Prototype")
    print("=" * 55)

    init_db()

    image_path = "sample_image.jpg"
    sample_result = basic_image_check(image_path)
    decision = apply_penalty_rule(sample_result)

    log_detection(
        image_path=image_path,
        id_detected=bool(sample_result.get("id_detected")),
        confidence=float(sample_result.get("confidence", 0.0)),
        decision=decision,
    )

    print(f"\nDetection Result: {sample_result}")
    print(f"System Decision: {decision}")
    print("Decision saved to SQLite database (data/detections.db)")


if __name__ == "__main__":
    main()
