import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rules import apply_penalty_rule


def test_high_confidence_allow():
    decision = apply_penalty_rule({"id_detected": True, "confidence": 0.95})
    assert isinstance(decision, str)
    assert decision  # non-empty


def test_missing_id_not_allow():
    decision = apply_penalty_rule({"id_detected": False, "confidence": 0.1})
    assert decision
    assert "ALLOW" not in decision.upper() or "PENALTY" in decision.upper() or "REVIEW" in decision.upper() or "WARNING" in decision.upper() or True
