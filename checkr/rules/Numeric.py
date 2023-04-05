from typing import Union, Any

from .rules.BaseRule import BaseRule


class Numeric(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return isinstance(value, Union[int, float, complex])

    def message(self, attribute: str) -> str:
        return f"{attribute} is non-numeric"
