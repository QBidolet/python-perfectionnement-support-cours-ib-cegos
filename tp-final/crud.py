from database import database_connection
from message import Message
from user import User


def add_user(user):
    with database_connection() as cursor:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))
        user.id = cursor.lastrowid
    return user


def get_user(user_id):
    with database_connection() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user_data = cursor.fetchone()
    if user_data:
        return User(*user_data)
    return None


def update_user(user):
    with database_connection() as cursor:
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (user.name, user.age, user.id))


def delete_user(user_id):
    with database_connection() as cursor:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))


def add_message(message):
    with database_connection() as cursor:
        cursor.execute("INSERT INTO messages (user_id, text) VALUES (?, ?)", (message.user_id, message.text))
        message.id = cursor.lastrowid
    return message


def get_message(message_id):
    with database_connection() as cursor:
        cursor.execute("SELECT * FROM messages WHERE id = ?", (message_id,))
        message_data = cursor.fetchone()
    if message_data:
        return Message(*message_data)
    return None


def update_message(message):
    with database_connection() as cursor:
        cursor.execute("UPDATE messages SET text = ? WHERE id = ?", (message.text, message.id))


def delete_message(message_id):
    with database_connection() as cursor:
        cursor.execute("DELETE FROM messages WHERE id = ?", (message_id,))
