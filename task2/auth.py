class AccessControl:

    def __init__(self):
        self.api_key = "jai123"

    def authenticate(self, user_key):
        if user_key == self.api_key:
            return True

        return False