from datetime import datetime
from typing import Any

from .BaseRule import BaseRule


class DateAfterOrEqual(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        specified_date = datetime.strptime(self.payload, "%Y-%m-%d")
        given_date = datetime.strptime(value, "%Y-%m-%d")
        return given_date >= specified_date

    def message(self, attribute: str) -> str:
        return f"{attribute} is not at {self.payload} or after"
