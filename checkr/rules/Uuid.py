from uuid import UUID
from typing import Any

from .BaseRule import BaseRule


class Uuid(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        version = self.payload or 4
        try:
            uuid_object = UUID(value, version=version)
        except ValueError:
            return False
        return str(uuid_object) == value

    def message(self, attribute: str) -> str:
        return f"'{attribute}' is not a valid UUID"
