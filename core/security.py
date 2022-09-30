import hashlib
import random
import string
from datetime import datetime, timedelta


def get_random_string(length=12):
    """ Generates random string for using like salt """
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(password: str, salt: str = None):
    """ Hashes password with salt """
    if salt is None:
        salt = get_random_string()
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


def validate_password(password: str, salt, hashed_password: str):
    """ Checks if password matches hash from database """
    return hash_password(password, salt) == hashed_password


