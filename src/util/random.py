from os import urandom
from base64 import b64encode

def sequence(n: 32) -> str:
    return b64encode(urandom(n)).decode('ascii')