import random
import string


def check_length(password: str) -> bool:
    """Check if the password hits the minimum length."""
    if len(password) < 8:
        return False
    else:
        return True


def check_uppercase(password: str) -> bool:
    """Check if the password has an uppercase letter."""
    for character in password:
        if character.isupper():
            return True
    return False


def check_lowercase(password: str) -> bool:
    """Check if the password has a lowercase letter."""
    for character in password:
        if character.islower():
            return True
    return False


def check_number(password: str) -> bool:
    """Check if the password has a number."""
    for character in password:
        if character.isdigit():
            return True
    return False


def check_special(password: str) -> bool:
    """Check if the password has a special character."""
    special_characters = "!@#$%^&*()-+"
    for character in password:
        if character in special_characters:
            return True
    return False


def check_password(password: str) -> bool:
    """Check if the password meets all the requirements."""
    # Chain of ifs to check if the password meets all the requirements. Simple.
    if not check_length(password):
        return False
    if not check_uppercase(password):
        return False
    if not check_lowercase(password):
        return False
    if not check_number(password):
        return False
    if not check_special(password):
        return False
    return True


def generate_password(max_length: int = 20) -> str:
    """Generate a password that meets the requirements."""
    # initialise the password length and base password
    password_length = random.randint(0, max_length)
    password = ""
    # create a password that meets the requirements
    while not check_password(password):
        password = ""
        # loop through the password length and add a random character
        for i in range(password_length):
            password += random.choice(string.ascii_letters + string.digits + "!@#$%^&*()-+")
    return password
