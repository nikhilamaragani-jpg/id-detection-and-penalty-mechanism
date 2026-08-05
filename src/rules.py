"""
Rule-based penalty / compliance logic for ID detection outcomes.
"""


def apply_penalty_rule(detection_result: dict) -> str:
    """
    Apply basic compliance rules based on detection output.

    Policy (prototype):
    - High-confidence ID present  -> allow / no penalty
    - ID missing or low confidence -> flag for review / warning path
    - Mid confidence               -> manual review
    """
    detected = bool(detection_result.get("id_detected"))
    confidence = float(detection_result.get("confidence", 0.0))

    if detected and confidence >= 0.8:
        return "ALLOW — ID detected with high confidence. No penalty."
    if detected and confidence >= 0.6:
        return "WARNING — Borderline confidence. Flag for manual review."
    if detected:
        return "REVIEW — ID signal weak. Escalate to security review."
    return "PENALTY_PATH — ID not clearly detected. Trigger compliance workflow (prototype)."
