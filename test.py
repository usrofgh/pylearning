from typing import Union


class BoolConversionError(Exception):
    """empty"""


def from_int(value: int) -> Union[bool, None]:
    if not isinstance(value, int):
        raise TypeError
    if value == 1:
        return True
    if value == 0:
        return False
    raise ValueError


def from_str(value: str) -> Union[bool, None]:
    if not isinstance(value, str):
        raise TypeError
    if value in ["True", "T", "1"]:
        return True
    if value in ["False", "F", "0"]:
        return False
    raise ValueError


def make_bool(value: Union[str, int]) -> Union[bool, None]:
    try:
        return from_int(value)
    except TypeError:
        try:
            return from_str(value)
        except TypeError:
            raise BoolConversionError(f"Cannot convert to the bool {type(value)} type")
        except ValueError:
            raise BoolConversionError(f"Cannot convert to the bool {value} value")
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")
