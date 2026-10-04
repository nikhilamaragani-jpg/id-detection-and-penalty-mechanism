"""
Rule-based penalty / compliance logic for ID detection outcomes.
"""

from collections.abc import Mapping
from typing import Any


def apply_penalty_rule(detection_result: Mapping[str, Any]) -> str:
    """
    Map a detector result to a review-first policy outcome.

    Policy (prototype):
    - High-confidence ID present  -> allow / no penalty
    - Mid-confidence ID present   -> warning / manual review
    - Low-confidence ID present   -> manual review
    - ID absent or unavailable    -> manual verification; never auto-penalize

    Raises:
        TypeError: If the result or its fields have unsupported types.
        ValueError: If confidence is missing or outside [0, 1].
    """
    if not isinstance(detection_result, Mapping):
        raise TypeError("detection_result must be a mapping")
    if "id_detected" not in detection_result or "confidence" not in detection_result:
        raise ValueError("detection_result must include id_detected and confidence")

    detected = detection_result.get("id_detected")
    confidence = detection_result.get("confidence")

    if detected is not None and not isinstance(detected, bool):
        raise TypeError("id_detected must be True, False, or None")

    if confidence is not None:
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
            raise TypeError("confidence must be a number or None")
        if not 0 <= confidence <= 1:
            raise ValueError("confidence must be finite and between 0 and 1")

    if detected is None:
        if confidence is not None:
            raise ValueError("confidence must be None when detection is unavailable")
        return "REVIEW: Detection unavailable. Verify the ID manually; no penalty applied."

    if confidence is None:
        raise ValueError("confidence is required when id_detected is True or False")

    if not detected:
        return "REVIEW: ID not detected. Verify manually before taking any action."

    if confidence >= 0.8:
        return "ALLOW: ID detected with high confidence. No penalty."
    if confidence >= 0.6:
        return "WARNING: Borderline confidence. Flag for manual review."
    return "REVIEW: ID signal weak. Escalate to manual review."
