from datetime import datetime, timedelta

date_format = "%Y.%m.%d"
days_ahead = 7
weekend_days = [5, 6]  # Saturday = 5, Sunday = 6

def get_upcoming_birthdays(users: list) -> list:
    """
    Check which users have birthdays within the next 7 days (including today).
    If the birthday falls on a weekend (Saturday or Sunday), 
    the congratulation date is moved to the following Monday.

    Args:
        users (list): A list of dictionaries, each with:
                      - 'name' (str): user's name
                      - 'birthday' (str): birthday in format 'YYYY.MM.DD'

    Returns:
        list: A list of dictionaries with:
              - 'name' (str): user's name
              - 'congratulation_date' (str): date in 'YYYY.MM.DD' format
    """
    
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], date_format).date()
        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= days_ahead:
            if birthday_this_year.weekday() in weekend_days:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime(date_format)
            })

    if upcoming_birthdays:
        upcoming_birthdays.sort(key=lambda x: x['congratulation_date'])
        print("Upcoming birthday congratulations:")
        for user in upcoming_birthdays:
            print(f"- {user['name']} : {user['congratulation_date']}")
    else:
        return "No birthdays in the next 7 days."


# test data
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Karl Buduar", "birthday": "1983.05.11"},
    {"name": "Jay Krakovic", "birthday": "1994.06.20"},
    {"name": "Ivan Mighty", "birthday": "1996.06.16"},
    {"name": "Monica Lineker", "birthday": "1989.04.22"},
    {"name": "Sara O'Conneli", "birthday": "1995.09.01"},
    {"name": "Sam Broker", "birthday": "1997.01.27"},
    {"name": "Sam Test", "birthday": "1997.06.17"},
]

birthdays = get_upcoming_birthdays(users)
print("Upcoming birthday congratulations:", birthdays)
