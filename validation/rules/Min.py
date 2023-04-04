from typing import Any, Union

from validation.rules.BaseRule import BaseRule


class Min(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        if isinstance(value, Union[int, float, complex]):
            return value >= int(self.payload)
        return len(value) >= int(self.payload)

    def message(self, attribute: str) -> str:
        return f"{attribute} length is smaller than {self.payload}"
