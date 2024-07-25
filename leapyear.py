from datetime import datetime, timedelta

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def adjust_anniversary(date):
    year = date.year
    if is_leap_year(year):
        next_anniversary = date.replace(year=year + 1)
        print(f"The year {year} is a leap year. The next anniversary is on {next_anniversary.strftime('%d/%m/%Y')}.")
    else:
        previous_anniversary = date.replace(year=year - 1)
        print(f"The year {year} is not a leap year. The previous anniversary was on {previous_anniversary.strftime('%d/%m/%Y')}.")
date_input = input("Enter Date (dd/mm/yyyy): ")
date = datetime.strptime(date_input, "%d/%m/%Y")
adjust_anniversary(date)
