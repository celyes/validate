import ulid
from typing import Any

from .BaseRule import BaseRule


class Ulid(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            ulid.parse(value)
        except ValueError:
            return False
        return True

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid ULID"
