import re
import string
import random




EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def generate_code(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))