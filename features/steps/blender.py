
class Blender(object):

    TRANSFORMATION_MAP = {
        "error message": "Enter a valid email"
    }

    def __init__(self):
        self.invalid_email = None
        self.error_message = None
        self.result = None

    @classmethod
    def select_result_for(cls, invalid_email):
        return cls.TRANSFORMATION_MAP.get(invalid_email, "invalid.email@.com")

    def add(self, invalid_email):
        self.invalid_email = invalid_email

    def switch_on(self):
        self.result = self.select_result_for(self.error_message)