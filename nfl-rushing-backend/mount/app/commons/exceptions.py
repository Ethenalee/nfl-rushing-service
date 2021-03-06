from enum import Enum


class AppErrorCode(str, Enum):
    INVALID_PARAMS = "INVALID_PARAMS"


class AppErrorMessage(str, Enum):
    INVALID_PARAMS = "invalid params"


class AppError(Exception):
    def __init__(self, code: AppErrorCode, message: str = ""):
        self.code = code.value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{repr(super())} code={self.code} message={self.message}>"


class InvalidParamError(AppError):
    def __init__(self, code: AppErrorCode, message: str = ""):
        super().__init__(code, message)
