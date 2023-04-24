import threading
from crud import add_user

def concurrent_function(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


@concurrent_function
def add_user_concurrently(user):
    return add_user(user)


@concurrent_function
def add_message_concurrently(message):
    return add_message(message)

# Vous pouvez également créer des fonctions concurrentes pour les autres opérations CRUD
