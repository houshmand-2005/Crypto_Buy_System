from django.core.validators import RegexValidator


def phone_validator(phone_number: str = "") -> str:
    return RegexValidator(
        regex=r"^\+{1}989\d{9}$",
        message="Phone number must be entered in the format: "
        "'+989xxxxxxxxx'. Up to 14 digits allowed.",
    )(phone_number)


def username_validator(username: str = "") -> str:
    return RegexValidator(
        regex=r"^[a-zA-Z0-9]+$",
        message="Username must consist of only English letters And without any spaces",
    )(username)
