from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email


def validate_email(value):
    desired_suffixs = ['gmail.com', '@mail.ru', '.org', '.net', '.edu', '.gov', '.mil', '.int']
    django_validate_email(value)
    if not any(value.endswith(suffix) for suffix in desired_suffixs):
        raise ValidationError("Invalid email address. Please make correct your email address.")
