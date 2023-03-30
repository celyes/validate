class InvalidRuleException(Exception):
    pass


class ValidationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class UnauthorizedRequestException(Exception):
    pass
