import json
from typing import Any

from .BaseRule import BaseRule


class Json(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        try:
            json.loads(value)
        except (ValueError, TypeError):
            return False
        return True

    def message(self, attribute: str) -> str:
        return f"{attribute} is not a valid JSON"
