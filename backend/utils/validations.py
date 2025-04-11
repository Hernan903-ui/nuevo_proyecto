import re

def is_valid_email(email):
    """
    Valida si el correo electrónico tiene un formato correcto.
    """
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def is_positive_number(value):
    """
    Verifica si un número es positivo.
    """
    return isinstance(value, (int, float)) and value > 0