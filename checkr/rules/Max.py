from typing import Any, Union

from checkr.rules.BaseRule import BaseRule


class Max(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        if isinstance(value, Union[int, float]):
            return value <= float(self.payload)
        return len(value) <= float(self.payload)

    def message(self, attribute: str) -> str:
        return f"{attribute} length is bigger than {self.payload}"
