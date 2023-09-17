# custom_errors.py
class Error(Exception):
    """Base class for all custom exceptions."""

    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)


class NoValueException(Error):
    """Raised when a required value is missing."""

    def __init__(self):
        message = "Some required values are missing."
        super().__init__(message)
