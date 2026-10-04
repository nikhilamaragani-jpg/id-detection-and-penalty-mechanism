import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rules import apply_penalty_rule


@pytest.mark.parametrize(
    ("confidence", "expected"),
    [
        (0.8, "ALLOW"),
        (0.6, "WARNING"),
        (0.59, "REVIEW"),
        (0, "REVIEW"),
        (1, "ALLOW"),
    ],
)
def test_detected_id_confidence_thresholds(confidence, expected):
    decision = apply_penalty_rule({"id_detected": True, "confidence": confidence})
    assert decision.startswith(expected)


def test_not_detected_id_requires_manual_review_even_at_high_confidence():
    decision = apply_penalty_rule({"id_detected": False, "confidence": 0.99})
    assert decision.startswith("REVIEW")
    assert "Verify manually" in decision
    assert "penalty" not in decision.lower()


def test_unavailable_detection_requires_manual_review():
    decision = apply_penalty_rule({"id_detected": None, "confidence": None})
    assert decision.startswith("REVIEW")
    assert "unavailable" in decision.lower()


@pytest.mark.parametrize("confidence", [-0.01, 1.01, float("nan"), float("inf")])
def test_rejects_invalid_confidence(confidence):
    with pytest.raises(ValueError, match="confidence"):
        apply_penalty_rule({"id_detected": True, "confidence": confidence})


@pytest.mark.parametrize("confidence", ["0.9", True])
def test_rejects_non_numeric_confidence(confidence):
    with pytest.raises(TypeError, match="confidence"):
        apply_penalty_rule({"id_detected": True, "confidence": confidence})


def test_rejects_invalid_detection_flag():
    with pytest.raises(TypeError, match="id_detected"):
        apply_penalty_rule({"id_detected": 1, "confidence": 0.9})


@pytest.mark.parametrize(
    "result",
    [
        {},
        {"id_detected": True},
        {"id_detected": False},
        {"id_detected": None, "confidence": 0.2},
    ],
)
def test_rejects_inconsistent_result(result):
    with pytest.raises(ValueError):
        apply_penalty_rule(result)


def test_rejects_non_mapping_result():
    with pytest.raises(TypeError, match="mapping"):
        apply_penalty_rule(None)
