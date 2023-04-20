class AuthException(Exception):
    pass   


class InvalidDateFormat(AuthException):
    def __init__(self):
        super().__init__('Date format is invalid!')    


class InvalidAmount(AuthException):
    def __init__(self):
        super().__init__('Invalid amount!')


class FileLoadingError(AuthException):
    def __init__(self):
        super().__init__('File loading failed!')    
