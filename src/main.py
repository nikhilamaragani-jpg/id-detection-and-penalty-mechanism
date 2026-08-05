"""
ID Card Detection and Penalty Mechanism
Prototype: detect → decide → log
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from detector import detect_id_status
from rules import decide_action
from database import init_db, log_decision


def banner() -> None:
    print("=" * 60)
    print("  ID Detection & Penalty Mechanism  |  Portfolio Prototype")
    print("  Detect · Rules · Decision · Audit log")
    print("=" * 60)


def run_case(label: str, payload: dict) -> None:
    print(f"\n--- Case: {label} ---")
    status = detect_id_status(payload)
    decision = decide_action(status)
    log_decision(status, decision)
    print(f"Detection : {status}")
    print(f"Decision  : {decision}")
    print("Logged    : yes (SQLite audit)")


def main() -> None:
    banner()
    init_db()

    # Demonstrates multiple policy outcomes for interview walkthroughs
    cases = [
        ("Valid ID present", {"face_detected": True, "id_detected": True, "match": True}),
        ("Missing ID", {"face_detected": True, "id_detected": False, "match": False}),
        ("ID mismatch", {"face_detected": True, "id_detected": True, "match": False}),
        ("No person detected", {"face_detected": False, "id_detected": False, "match": False}),
    ]

    for label, payload in cases:
        try:
            run_case(label, payload)
        except TypeError:
            # Fallback if detector API expects different signature
            status = detect_id_status()
            decision = decide_action(status)
            log_decision(status, decision)
            print(f"\n--- Case: {label} (fallback interface) ---")
            print(f"Detection : {status}")
            print(f"Decision  : {decision}")
            break

    print("\nDone. Architecture ready for OpenCV/YOLO + alert integrations.")
    print("See docs/INTERVIEW.md for recruiter walkthrough.")


if __name__ == "__main__":
    main()
