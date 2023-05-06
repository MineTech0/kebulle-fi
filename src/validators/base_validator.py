class BaseValidator():
    errors = []

    def validate(self, form):
        pass

    def notEmpty(self, str):
        return str is not None and str != ''

    def inRange(self, num, min_value, max_value):
        num = int(num)
        return num >= min_value and num <= max_value

    def isBoolean(self, bool_value):
        return bool_value is True or bool_value is False

    def getErrors(self):
        return self.errors
