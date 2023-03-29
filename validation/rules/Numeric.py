from abc import abstractmethod
from typing import Union

from validation.rules.BaseRule import BaseRule


class Numeric(BaseRule):
    def validate(self, attribute, value) -> bool:
        return isinstance(value, Union[int, float, complex])

    def message(self) -> str:
        return 'field value is non-numeric'
