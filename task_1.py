from datetime import datetime

def get_days_from_today(date: str, format: str = "%Y-%m-%d") -> int:
    """
    Calculate the number of days between today and a given date.

    Args:
        date (str): The date string to compare with today.
        format (str, optional): The format of the date string. Defaults to "%Y-%m-%d".

    Returns:
        int: The number of days between today and the given date.

    Raises:
        ValueError: If the date string is not in the correct format.
    """
    try:
        date_object = datetime.strptime(date, format).date()
        today = datetime.today().date()
        delta = today - date_object
        return delta.days
    except ValueError:
        raise ValueError("The date string is not in the correct format. Please use 'YYYY-MM-DD'.")

print(get_days_from_today("2026-12-31")) 
