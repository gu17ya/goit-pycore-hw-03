import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers for a lottery ticket.

    Args:
        min_number (int): Minimum possible number (must be >= 1)
        max_number (int): Maximum possible number (must be <= 1000)
        quantity (int): How many unique numbers to generate (must be > 0 and <= range size)

    Returns:
        list[int]: Sorted list of unique random numbers or empty list if inputs invalid
    """

    # Validate input parameters
    if min_number < 1:
        print(f"❌ Invalid input: min_number must be ≥ 1. You entered {min_number}.")
        return []
    if max_number > 1000:
        print(f"❌ Invalid input: max_number must be ≤ 1000. You entered {max_number}.")
        return []
    if min_number > max_number:
        print("❌ Invalid input: min_number > max_number.")
        return []
    if quantity <= 0:
        print(f"❌ Invalid input: quantity must be > 0. You entered {quantity}.")
        return []
    if quantity > (max_number - min_number + 1):
        print("❌ Invalid input: quantity is too large for the given range.")
        return []

    # Generate unique random numbers in range and sort them
    numbers = random.sample(range(min_number, max_number + 1), quantity)
    return sorted(numbers)


print("Your lottery numbers:", get_numbers_ticket(1, 90, 10))
