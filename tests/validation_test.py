import pytest

from checkr import validate
from tests.fixtures import (
    SampleRequestUsingArrayRules,
    SampleRequest,
    SampleRequestWithIncorrectRule,
    SampleRejectedRequest,
    SampleFailingRequest,
)
from checkr.exceptions import (
    InvalidRuleException,
    UnauthorizedRequestException,
    ValidationError,
)


def test_reject_request_if_unauthorized():
    request = {}
    validation_class = SampleRejectedRequest()
    with pytest.raises(UnauthorizedRequestException):
        validate(validation_class=validation_class, request_data=request)


def test_can_validate_array_of_rules():
    request = {"foo": "bar"}
    validation_class = SampleRequestUsingArrayRules()
    assert validate(validation_class=validation_class, request_data=request) is True


def test_can_validate_string_of_rules():
    request = {"foo": "bar"}
    validation_class = SampleRequest()
    assert validate(validation_class=validation_class, request_data=request) is True


def test_throws_correct_exception_when_rule_is_incorrect():
    request = {}
    validation_class = SampleRequestWithIncorrectRule()
    with pytest.raises(InvalidRuleException):
        validate(validation_class=validation_class, request_data=request)


def test_throws_correct_exception_when_validation_fails():
    request = {}
    validation_class = SampleFailingRequest()
    with pytest.raises(ValidationError):
        validate(validation_class=validation_class, request_data=request)
