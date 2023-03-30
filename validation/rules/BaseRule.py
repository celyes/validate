from abc import ABCMeta
from typing import Any


class BaseRule(metaclass=ABCMeta):

    payload = None

    def __str__(self):
        return __class__

    def validate(self, attribute: str, value: Any) -> bool:
        raise NotImplementedError

    def message(self) -> str:
        pass

    def set_validation_payload(self, payload):
        self.payload = payload
