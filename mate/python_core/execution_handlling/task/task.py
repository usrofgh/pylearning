class InvalidUsername(Exception):
    """empty"""


class PasswordMissmatch(Exception):
    """empty"""


class ValidationError(Exception):
    """empty"""


class DBUserCreationError(Exception):
    """empty"""


def username_validation(username: str) -> None:
    if len(username) < 4 or len(username) > 15:
        raise InvalidUsername("InvalidUsername !")


def password_validation(password1: str, password2: str) -> None:
    if password1 != password2:
        raise PasswordMissmatch


def user_validation(data: dict) -> None:
    try:
        username_validation(data["username"])
    except InvalidUsername:
        raise ValidationError

    try:
        password_validation(data["password1"], data["password2"])
    except PasswordMissmatch:
        raise ValidationError


def db_user_creation(user: dict) -> None:
    try:
        user_validation(user)
    except ValidationError:
        raise DBUserCreationError
    else:
        print(f"{user['username']} is created in the database")


db_user_creation(
    user={"username": "UsernameUsername",
          "password1": "password",
          "password2": "password"},
)
#  DBUserCreationError
