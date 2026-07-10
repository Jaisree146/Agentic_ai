class Security:

    def __init__(self):

        self.blocked_patterns = [
            "ignore previous instructions",
            "ignore all previous instructions",
            "forget previous instructions",
            "system prompt",
            "developer prompt",
            "reveal prompt",
            "reveal system prompt",
            "change your role",
            "act as",
            "instead of",
            "pretend you are",
            "ignore your role"
        ]

    def check_prompt(self, text):

        text = text.lower()

        for pattern in self.blocked_patterns:
            if pattern in text:
                return False

        return True