from typing import Any, List, Optional, Sequence, Tuple

from pyvnt.exceptions import ValidationException
from pyvnt.utilities import MessageFactory
from pyvnt.validator import Validator


def has_length(length: int, message: Optional[MessageFactory[Sequence[Any]]] = None) -> Validator[Sequence[Any]]:
    """Checks if the property has exactly the specified length. Works only with `Sequence` types.

    Args:
        length (int): The length you want to check against."""

    def predicate(value: Sequence[Any], property_name: str) -> Tuple[bool, List[ValidationException]]:
        return len(value) == length, []

    def message_factory(value: Sequence[Any], property_name: str, negate: bool):
        return f"Expected property \"{property_name}\" to{' not ' if negate else ' '}have length \"{length}\"."

    return Validator(name="has_length", predicate=predicate, message_factory=message or message_factory)
