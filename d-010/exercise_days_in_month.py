"""
-=< 100 Days of Python >=-
-=[ Day 010 ]=-

Coding Exercise: Days in Month (L.102)
Ref: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/79040aa6-f9d2-4493-9f92-52c26748ec3e?sl=c9278fb9-a6f0-492d-9547-fb79a3eadc76&st=xPEfb67hnFBbXQXPw9pBURtadKusnZIV
"""
"""
Slide 1: Task
- Write a program that will take a Year and a Month as inputs and calculate
how many days are in the given month.

For this we will start by converting the "leap year" exercise from Day-003,
turning it in to a function which returns True of False for a given Year.
"""


def is_leap(test_year):
    """determine if a year is a 'Leap-Year' or not"""
    # 1. If year is not evenly divisible by 4 then it is NOT a leap year!
    if test_year % 4 != 0:
        return False

    # In all cases where year IS evenly divisible by 4...
    # 2. If the year is NOT evenly divisible by 100 then it IS a leap year!
    if test_year % 100 != 0:
        return True

    # 3. Year IS evenly divisible by 100 so...
    # If the year is NOT evenly divisible by 400 then it is NOT a leap year!
    if test_year % 400 != 0:
        return False

    # 4. Finally, in ALL other cases it IS a leap year!
    return True


"""
Slide 2: Solution
"""


def days_in_month(test_year, test_month):
    """determine how many days are in a given month, in a given year"""
    # provide a look-up library (List)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # grab the standard number of days (accounting for zero index)
    number_of_days = month_days[test_month-1]
    # correct for leap years
    if is_leap(test_year) and test_month == 2:
        number_of_days += 1
    # return the value
    return number_of_days


# Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
