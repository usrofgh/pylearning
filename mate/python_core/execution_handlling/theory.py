# -----------------------------------------------------------------------------------------------------------
# info from here https://mate.academy/learn/python-core/python-core-exception-handling#/theory
# There are 3 types of errors in Python: compile-time errors; run-time errors; logical errors


# compile-time
#  before run program, the source code must be compiled into the machine code
#  if have wrong comma etc, var like sum/type/int, str doesn't have quotes , not all brackets


#  Run-Time Error. occurs during run-time.  Also calls exceptions
#  division by zero; calling unexisting var/file; operating on incompatible types;

# Logical Error. Program works, but incorrect result
#  wrong var name; integer division instead of floating-point division; mistake in a boolean expression.

class CanRideExtremeException(Exception):
    min_age = 18
    max_age = 45

    def __init__(self, age, *args):
        super().__init__(args)
        self.age = age

    def __str__(self):
        return f"The age {self.age} is not in a valid range {self.min_age} - {self.max_age}."


def can_ride(age: int) -> bool:
    # if (age <= CanRideExtremeException.min_age) or (age >= CanRideExtremeException.max_age):
    #     raise CanRideExtremeException(age)  # CanRideExtremeException: The age 18 is not in a valid range 18 - 45.
    return True


print(can_ride(19))  # True
print(can_ride(18))  # __main__.CanRideExtremeException: The age 18 is not in a valid range 18 - 45.
# -----------------------------------------------------------------------------------------------------------
# info from here https://realpython.com/python-exceptions/
import sys

print("linux" in sys.platform)  # False
# assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
# assert "linux" in sys.platform, "it isn't linux"  # AssertionError: it isn't linux
# don't use assert often cause it's more difficult to catch than exceptions
# -----------------------------------------------------------------------------------------------------------
# https://mate.academy/learn/python-core/python-core-exception-handling#/video/2125

condition = True
str_n = "10.3"

def is_error(condition: bool, str_n):
    try:
        if condition:
            int(str_n)
        else:
            5 + "5"
    except ValueError as err:
        print(err)
    except TypeError as err:
        print(err)
    else:
        print("Not exceptions")
    finally:
        print("do it anyway")


is_error(condition, str_n)  # invalid literal for int() with base 10: '10.3'; do it anyway
condition = False
is_error(condition, str_n)  # unsupported operand type(s) for +: 'int' and 'str'; do it anyway
str_n = "10"
condition = True
is_error(condition, str_n)  # Not exceptions; do it anyway
# -----------------------------------------------------------------------------------------------------------
# https://mate.academy/learn/python-core/python-core-exception-handling#/video/2130

# we need CustomError as a parent for catch 2+ custom errors. Cause we specify "except CustomError as e"


class CustomError(Exception):
    """empty"""


class ValueTooBigError(CustomError):
    def __init__(self, message="Value should be <= 10"):
        super().__init__(message)


class ValueTooSmallError(CustomError):
    """empty"""


value = 11
try:
    if value > 10:
        raise ValueTooBigError  # Value should be <= 10 // we cen redefine raise error text in a custom exception class
    if value < 5:
        raise ValueTooSmallError(f"{value} is too small")

    print(f"{value} is ok!")
except CustomError as e:
    print("Handled errors:")
    print(e)
