from enum import Enum

import pytest
from clocktower_evidence_lab.domain.primitives import Derivation, SemanticId, Verification
from pydantic import TypeAdapter, ValidationError


def test_evidence_status_axes_are_independent_string_enums() -> None:
    assert issubclass(Derivation, str)
    assert issubclass(Derivation, Enum)
    assert [item.value for item in Derivation] == [
        "OBSERVED",
        "RECONSTRUCTED",
        "INFERRED",
        "UNKNOWN",
        "NOT_APPLICABLE",
    ]

    assert issubclass(Verification, str)
    assert issubclass(Verification, Enum)
    assert [item.value for item in Verification] == [
        "UNVERIFIED",
        "VERIFIED",
        "DISPUTED",
    ]


def test_semantic_id_preserves_valid_external_identity() -> None:
    adapter = TypeAdapter(SemanticId)

    assert adapter.validate_python("source:youtube:qZBvRfM3Xow") == "source:youtube:qZBvRfM3Xow"


@pytest.mark.parametrize("value", ["", " ", "\tbad", "bad\n", " padded "])
def test_semantic_id_rejects_blank_or_whitespace_wrapped_values(value: str) -> None:
    adapter = TypeAdapter(SemanticId)

    with pytest.raises(ValidationError):
        adapter.validate_python(value)


def test_semantic_id_rejects_unbounded_identifiers() -> None:
    adapter = TypeAdapter(SemanticId)

    with pytest.raises(ValidationError):
        adapter.validate_python("x" * 129)
