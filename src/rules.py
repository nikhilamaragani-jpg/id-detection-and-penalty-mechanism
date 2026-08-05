"""
Simple rule-based penalty / compliance logic
"""

def apply_penalty_rule(detection_result: dict) -> str:
    """
    Applies a basic rule based on detection output.
    """
    if detection_result.get("id_detected") and detection_result.get("confidence", 0) > 0.7:
        return "ID detected with sufficient confidence. No penalty triggered (prototype)."
    else:
        return "ID not clearly detected. Flag for manual review (prototype)."
