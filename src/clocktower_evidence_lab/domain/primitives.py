"""Small durable primitives shared by evidence-domain entities."""

from enum import StrEnum
from typing import Annotated

from pydantic import AfterValidator

_MAX_SEMANTIC_ID_LENGTH = 128


def _validate_semantic_id(value: str) -> str:
    if not value:
        raise ValueError("semantic ID must not be empty")
    if value != value.strip() or any(character.isspace() for character in value):
        raise ValueError("semantic ID must not contain whitespace")
    if len(value) > _MAX_SEMANTIC_ID_LENGTH:
        raise ValueError(f"semantic ID must be at most {_MAX_SEMANTIC_ID_LENGTH} characters")
    return value


type SemanticId = Annotated[str, AfterValidator(_validate_semantic_id)]


class Derivation(StrEnum):
    """How a claim was obtained from evidence."""

    OBSERVED = "OBSERVED"
    RECONSTRUCTED = "RECONSTRUCTED"
    INFERRED = "INFERRED"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class Verification(StrEnum):
    """Independent verification state for an evidence claim."""

    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    DISPUTED = "DISPUTED"
