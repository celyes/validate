from typing import Any, Union

from validation.rules.BaseRule import BaseRule


class Max(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        if isinstance(value, Union[int, float]):
            return value <= float(self.payload)
        return len(value) <= int(self.payload)

    def message(self, attribute: str) -> str:
        return f"{attribute} length is bigger than {self.payload}"
