import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize a Ukrainian phone number to the standard international format: +380XXXXXXXXX.

    Args:
        phone_number (str): The raw phone number in various formats.

    Returns:
        str: Normalized phone number in format +380XXXXXXXXX.
    """

    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone_number)

    # If the number starts with '380', assume it's a full Ukrainian number and add '+'
    if digits.startswith('380'):
        return '+' + digits

    # If the number starts with '0', replace it with '+38'
    if digits.startswith('0'):
        return '+38' + digits

    # If the number is missing both '+' and country code, prepend '+380'
    return '+380' + digits


phone_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [normalize_phone(number) for number in phone_numbers]
print("Normalized phone numbers for SMS delivery:", sanitized_numbers)