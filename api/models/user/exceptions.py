"""Exceptions related to user related operations"""


class WrongEmailCode(BaseException):
    """Raised when the wrong code is supplied during email validation"""


class WrongPhoneCode(BaseException):
    """Raised when the wrong code is supplied during phone validation"""


class WrongPasswordResetCode(BaseException):
    """Raised when the wrong password reset code is submitted"""


class PhoneValidationLimitExceeded(BaseException):
    """Raised when the time limit between consecutive phone validation attempts is exceeded"""


class PhoneNumberNotSet(BaseException):
    """Raised when there is no phone number set for user"""

class NotAGmailUser(BaseException):
    """Raised when the user is not a gmail user but it's needed for an operation"""