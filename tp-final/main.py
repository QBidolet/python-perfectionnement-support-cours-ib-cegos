from concurrency import add_user_concurrently, add_message_concurrently
from crud import (add_user, get_user, update_user, delete_user,
                  add_message, get_message, update_message, delete_message)
from message import Message
from user import User


def main():
    # Exemple d'utilisation des opérations CRUD pour les utilisateurs
    user = User(None, "Alice", 30)
    user = add_user(user)
    print(f"User ajouté : {user}")

    fetched_user = get_user(user.id)
    print(f"Utilisateur récupéré : {fetched_user}")

    user.name = "Bob"
    user.age = 35
    update_user(user)
    print(f"Utilisateur mis à jour : {user}")

    delete_user(user.id)
    print(f"Utilisateur supprimé : {user.id}")

    # Exemple d'utilisation des opérations CRUD pour les messages
    message = Message(None, user.id, "Hello, world!")
    message = add_message(message)
    print(f"Message ajouté : {message}")

    fetched_message = get_message(message.id)
    print(f"Message récupéré : {fetched_message}")

    message.text = "Updated message"
    update_message(message)
    print(f"Message mis à jour : {message}")

    delete_message(message.id)
    print(f"Message supprimé : {message.id}")

    # Exemple d'utilisation des fonctions concurrentes
    user = User(None, "Alice", 30)
    thread = add_user_concurrently(user)
    thread.join()

    message = Message(None, user.id, "Hello, world!")
    thread = add_message_concurrently(message)
    thread.join()


if __name__ == "__main__":
    main()
