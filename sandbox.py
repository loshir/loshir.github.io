from datetime import date, timedelta

def get_current_week_days():
    """Returns an array of day numbers (1-31) for the current week."""
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())  # Monday
    week_days = [start_of_week + timedelta(days=i) for i in range(7)]
    return [day.day for day in week_days]  # Extract day of the month (1-31)

# Example usage
print(get_current_week_days())  # Output: [6, 7, 8, 9, 10, 11, 12] (for Oct 2025)
