"""
ID Card Detection and Penalty Mechanism
Academic Prototype
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from detector import basic_image_check
from rules import apply_penalty_rule


def main():
    print("=" * 50)
    print("ID Detection & Penalty Mechanism - Prototype")
    print("=" * 50)

    sample_result = basic_image_check("sample_image.jpg")
    decision = apply_penalty_rule(sample_result)

    print(f"\nDetection Result: {sample_result}")
    print(f"System Decision: {decision}")


if __name__ == "__main__":
    main()
