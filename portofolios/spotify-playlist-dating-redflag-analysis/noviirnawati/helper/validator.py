import validators
from validators import ValidationError

from ..constant.constant import Generic


def validate_url(url_to_validate: str) -> bool:
    try:
        result = validators.url(url_to_validate)
        if isinstance(result, ValidationError):
            return False
        return result
    except ValidationError:
        return False


def dct_is_empty_or_none(dct: dict) -> bool:
    return None is dct and {} != dct


def str_is_empty_or_none(string: str) -> bool:
    return string == Generic.EMPTY_STRING or string is None
