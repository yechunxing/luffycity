class BaseResponse(object):
    def __init__(self):
        self.code = 0
        self.data = None
        self.error = None
    @property
    def dict(self):
        return self.__dict__