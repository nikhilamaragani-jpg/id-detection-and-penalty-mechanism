"""
ID Card Detection and Penalty Mechanism
Academic Prototype
"""

from detector import basic_image_check
from rules import apply_penalty_rule


def main():
    print("=" * 50)
    print("ID Detection & Penalty Mechanism - Prototype")
    print("=" * 50)

    # Demo flow (replace with real image processing later)
    sample_result = basic_image_check("sample_image.jpg")
    decision = apply_penalty_rule(sample_result)

    print(f"\nDetection Result: {sample_result}")
    print(f"System Decision: {decision}")


if __name__ == "__main__":
    main()
