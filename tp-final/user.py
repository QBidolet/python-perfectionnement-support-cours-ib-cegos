class UserMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        if instance.age < 0:
            raise ValueError("L'âge doit être supérieur ou égal à 0")
        return instance

class User(metaclass=UserMeta):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
