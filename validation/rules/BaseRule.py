from abc import ABCMeta


class BaseRule(metaclass=ABCMeta):

    def __str__(self):
        return __class__

    def validate(self, attribute, value) -> bool:
        raise NotImplementedError

    def message(self) -> str:
        pass
