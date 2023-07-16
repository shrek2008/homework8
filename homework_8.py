from datetime import datetime, timedelta

# Test data
users = [
    {"name": "Pitier", "birthday": datetime(1990, 7, 19)},
    {"name": "Angel", "birthday": datetime(2000, 6, 24)},
    {"name": "Angelina", "birthday": datetime(1985, 7, 17)},
    {"name": "Bill", "birthday": datetime(1988, 7, 17)},
    {"name": "Kim", "birthday": datetime(2001, 7, 20)},
    {"name": "Jan", "birthday": datetime(2002, 7, 25)},
]

def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5 - current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()

def get_birthdays_per_week(users):
    result = {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    current_year = datetime.now().year

    for user in users:
        bd = user["birthday"]
        bd_date = bd.date()  # Convert datetime to date
        bd_date = bd_date.replace(year=current_year)

        start, end = get_period()
        if start <= bd_date <= end:
            # Calculate the birthday weekday, considering Monday as the start of the week (0 index).
            if bd_date.weekday() in (5, 6):  # Saturday (5) or Sunday (6)
                # For users with birthdays on weekends, consider Monday as their "birthday week" day.
                result["Monday"].append(user["name"])
            else:
                # For users with birthdays on weekdays, add their names based on the weekday.
                result[bd_date.strftime("%A")].append(user["name"])

    # Print the result
    for day, names in result.items():
        if names:
            print(f"{day}: {', '.join(names)}")

if __name__ == "__main__":
    get_birthdays_per_week(users)
