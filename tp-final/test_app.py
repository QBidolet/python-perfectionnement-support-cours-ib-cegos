# pip install pytest
# pytest test_app.py
import pytest

from crud import add_user, add_message, update_user, update_message, delete_user, delete_message, get_message, get_user
from message import Message
from user import User


def test_user_age_validation():
    with pytest.raises(ValueError):
        User(1, "Alice", -1)


def test_message_length_validation():
    with pytest.raises(ValueError):
        Message(1, 1, "")

    with pytest.raises(ValueError):
        Message(1, 1, "A" * 141)


def test_crud_operations():
    user = User(None, "Alice", 30)
    user = add_user(user)
    assert user.id is not None

    fetched_user = get_user(user.id)
    assert fetched_user.id == user.id
    assert fetched_user.name == user.name
    assert fetched_user.age == user.age

    user.name = "Bob"
    user.age = 35
    update_user(user)

    fetched_user = get_user(user.id)
    assert fetched_user.name == "Bob"
    assert fetched_user.age == 35

    message = Message(None, user.id, "Hello, world!")
    message = add_message(message)
    assert message.id is not None

    fetched_message = get_message(message.id)
    assert fetched_message.id == message.id
    assert fetched_message.user_id == message.user_id
    assert fetched_message.text == message.text

    message.text = "Updated message"
    update_message(message)

    fetched_message = get_message(message.id)
    assert fetched_message.text == "Updated message"

    delete_message(message.id)
    assert get_message(message.id) is None

    delete_user(user.id)
    assert get_user(user.id) is None
