from datetime import datetime, timedelta

def get_current_date():
    """
    Devuelve la fecha y hora actual.
    """
    return datetime.now()

def format_date(date, fmt='%Y-%m-%d %H:%M:%S'):
    """
    Formatea una fecha al formato especificado.
    """
    return date.strftime(fmt)

def add_days_to_date(date, days):
    """
    Agrega un número de días a una fecha.
    """
    return date + timedelta(days=days)