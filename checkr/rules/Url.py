import validators
from typing import Any

from .BaseRule import BaseRule


class Url(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return validators.url(value or "")

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid URL"
