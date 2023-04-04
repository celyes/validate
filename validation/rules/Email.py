from typing import Any
import validators
from validators import ValidationFailure

from validation.rules.BaseRule import BaseRule


class Email(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            return validators.email(value)
        except ValidationFailure:
            return False

    def message(self, attribute: str) -> str:
        return f"`{attribute}` does not start with the `{self.payload}`"
