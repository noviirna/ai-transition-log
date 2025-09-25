import validators
from validators import ValidationError


def validate_url(url_to_validate: str):
    try:
        result = validators.url(url_to_validate)
        if isinstance(result, ValidationError):
            return False
        return result
    except:
        return False
    finally:
        print("validating url finish")
