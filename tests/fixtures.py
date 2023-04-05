from typing import Dict

from .BaseRequest import BaseRequest


class SampleRequest(BaseRequest):
    @staticmethod
    def authorize() -> bool:
        return True

    @staticmethod
    def rules() -> Dict:
        return {
            "foo": "required",
        }


class SampleFailingRequest(BaseRequest):
    @staticmethod
    def authorize() -> bool:
        return True

    @staticmethod
    def rules() -> Dict:
        return {
            "foo": "required",
        }


class SampleRequestUsingArrayRules(BaseRequest):
    @staticmethod
    def authorize() -> bool:
        return True

    @staticmethod
    def rules() -> Dict:
        return {
            "foo": ["required", "string"],
        }


class SampleRequestWithIncorrectRule(BaseRequest):
    @staticmethod
    def authorize() -> bool:
        return True

    @staticmethod
    def rules() -> Dict:
        return {
            "foo": "bar",
        }


class SampleRejectedRequest(BaseRequest):
    @staticmethod
    def authorize() -> bool:
        return False

    @staticmethod
    def rules() -> Dict:
        return {
            "foo": "bar",
        }
