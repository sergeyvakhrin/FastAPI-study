from pydantic import ValidationError

from models.user import User


def foo_1():
    user1 = User(id=1, name="Alice", email="alice@example.com")
    print(user1)
    print(user1.greet())


def foo_2():
    try:
        user2 = User(id=-1, name="Bob", email="invalid-email", age=-5)
    except ValidationError as e:
        print(e.json())
