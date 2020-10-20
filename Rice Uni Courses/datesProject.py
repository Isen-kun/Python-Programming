"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates
"""

import datetime


def days_in_month(year, month):
    """
    Takes input year and month and returns number of date in the
    """
    date1 = datetime.date(year, month, 1)
    if month == 12:
        date2 = datetime.date(year+1, 1, 1)
    else:
        date2 = datetime.date(year, month+1, 1)
    return (date2-date1).days


def is_valid_date(year, month, day):
    """
    Takes input of year,month,day and return True if year-month-day is a valid date
    """
    if year >= datetime.MINYEAR and year <= datetime.MAXYEAR:
        if month >= 1 and month <= 12:
            if day >= 1 and day <= days_in_month(year, month):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Takes input of two sets of year,month,day and return the number of days in between
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        differ = (date2-date1).days
        if(differ >= 0):
            return differ
        else:
            return 0
    else:
        return 0


def age_in_days(year, month, day):
    """
    Takes input of year,month,day and returns the difference from today's
    """
    if is_valid_date(year, month, day):
        today = datetime.date.today()
        return days_between(year, month, day, today.year, today.month, today.day)
    else:
        return 0
