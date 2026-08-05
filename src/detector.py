"""
Basic detection module (placeholder)
"""

def basic_image_check(image_path: str) -> dict:
    """
    Placeholder detection function.
    In a full version, this would use OpenCV / object detection.
    """
    print(f"Checking image: {image_path}")

    # Simulated result for prototype
    return {
        "id_detected": True,
        "confidence": 0.82,
        "notes": "Prototype result - replace with real CV model"
    }
