def is_leap_meh(year):
    # if the year is divisible by 100 it is not a leap year unless it's also divisible by 4
    leap = False

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False

    return leap


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
