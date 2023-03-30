from abc import abstractmethod
from typing import Union, Any

from validation.rules.BaseRule import BaseRule


class InArray(BaseRule):
    def validate(self, attribute: str, value: Any) -> bool:
        return value in self.payload

    def message(self) -> str:
        return 'field value is not in the given list'
