"""
ID Card Detection and Penalty Mechanism
Prototype: detect → decide → log
"""

import sys
import os
from typing import Dict, Optional

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from detector import basic_image_check
from rules import apply_penalty_rule
from database import init_db, log_detection


def banner() -> None:
    print("=" * 60)
    print("  ID Detection & Penalty Mechanism  |  Portfolio Prototype")
    print("  Detect · Rules · Decision · Audit log")
    print("=" * 60)


def run_case(label: str, image_path: str, simulated: Optional[Dict] = None) -> None:
    print(f"\n--- Case: {label} ---")
    if simulated is None:
        result = basic_image_check(image_path)
    else:
        result = simulated
        print(f"Checking image: {image_path} (simulated scenario)")

    decision = apply_penalty_rule(result)
    log_detection(
        image_path=image_path,
        id_detected=bool(result.get("id_detected")),
        confidence=float(result.get("confidence", 0.0)),
        decision=decision,
    )
    print(
        f"Detection : id_detected={result.get('id_detected')} "
        f"confidence={result.get('confidence')}"
    )
    print(f"Decision  : {decision}")
    print("Logged    : yes (SQLite audit)")


def main() -> None:
    banner()
    init_db()

    cases = [
        (
            "Valid ID present (high confidence)",
            "samples/valid_id.jpg",
            {"id_detected": True, "confidence": 0.91, "notes": "Simulated valid ID"},
        ),
        (
            "Missing / unclear ID (low confidence)",
            "samples/missing_id.jpg",
            {"id_detected": False, "confidence": 0.22, "notes": "Simulated missing ID"},
        ),
        (
            "Borderline detection (manual review)",
            "samples/borderline.jpg",
            {"id_detected": True, "confidence": 0.55, "notes": "Simulated borderline"},
        ),
        (
            "Default detector path",
            "samples/camera_frame.jpg",
            None,
        ),
    ]

    for label, path, simulated in cases:
        run_case(label, path, simulated)

    print("\nDone. Architecture ready for OpenCV/YOLO + alert integrations.")
    print("See docs/INTERVIEW.md for recruiter walkthrough.")


if __name__ == "__main__":
    main()
