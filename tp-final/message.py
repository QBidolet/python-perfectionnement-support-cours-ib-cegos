class Message:
    def __init__(self, id, user_id, text):
        self.id = id
        self.user_id = user_id
        self.text = self.validate_message(140)(text)

    @staticmethod
    def validate_message(max_length):
        def validator(text):
            if len(text) > max_length or len(text) == 0:
                raise ValueError(f"Le message doit avoir entre 1 et {max_length} caractères")
            return text
        return validator
