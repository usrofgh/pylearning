# https://mate.academy/learn/python-core/python-core-exception-handling#/practice/python_admin_required_exception

from typing import Callable


class UnauthenticatedError(Exception):
    pass


class PermissionDeniedError(Exception):
    pass


def login_required(func: Callable) -> Callable:
    def inner(request: dict) -> None:
        if "user" not in request:
            raise UnauthenticatedError("Authentication credentials were not provided!")
        func(request)
    return inner


def admin_required(func: Callable) -> Callable:
    def inner(request: dict) -> None:
        if not request["user"]["is_admin"]:
            raise PermissionDeniedError("User must be admin!")
        func(request)
    return inner


@login_required
@admin_required
def access_admin_page(request: dict) -> None:
    print(f"Welcome to the admin page, {request['user']['full_name']}")

