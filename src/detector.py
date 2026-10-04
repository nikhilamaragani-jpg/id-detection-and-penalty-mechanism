"""Detection adapter for the ID verification workflow."""


def basic_image_check(image_path: str) -> dict:
    """Return an explicit unavailable result until a real CV model is configured."""
    return {
        "id_detected": None,
        "confidence": None,
        "notes": f"No detector is configured for {image_path!r}.",
    }
