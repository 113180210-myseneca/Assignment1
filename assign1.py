#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2021
Program: assign1.py (replace student_id with your Seneca User name)
Author: Parkhi Sharma
The python code in this file (assign1.py) is original work written by
Parkhi Sharma. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: The python script returns date in a DD-MM-YYYY format when provided with the correct number and format of arguments.

Date: 7/8/2023 
'''
import sys

def usage():
    "This function defines th usage of the arguments in command line."
    print("Please follow the below format when using this script in order to receive the correct output. Provide the date in the DD-MM-YYYY format and the number of day as X.")
    print("python3 assign1.py DD-MM-YYYY X")

def days_in_mon(year):
    " This fucntion sets the maximum number of days in each month."
    # Defining a variable for the leap_year function which we will defining later.
    lyear= leap_year(year)
    # Setting the maximum number of days for each month, also defining the maximum number of day for February depending upon if it is a leap year or not.
    days_in_month = { 1:31, 2:29 if lyear else 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return days_in_month

def leap_year(year):
    "Defines whether the year value is a leap year or not. If the year is"
    "divisible by 4 then it must also be divisible by 100 or 400 for the "
    "condition to be True."
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def valid_date(date):
    "This function checks if the arguments given by the user are valid or"
    "not in order to be used by the script. If they are valid, script will not show any error."
    try:
        # Divides the given argument into year, month and day.
        day, month, year = map(int, date.split('-'))
        # Uses the dictionary for the number of days in each month
        days_in_month = days_in_mon(year)
        # Confirms if the values for day, month and year actually exist or not
        if month < 1 or month > 12:
            return False, "Error: wrong month entered"
        if day < 1 or day > days_in_month[month]:
            return False, "Error: wrong day entered"
        return True, ""
    except ValueError:
        return False, "Error: wrong date entered"

def after(today):
    "Accepts a date in the DD-MM-YYYY format and returns the output"
    "as the next day in the same format."
    # Checking the validity of the date.
    valid, error = valid_date(today)
    if not valid:
        return error
    # Divides the given argument into year, month and day.
    day, month, year = map(int, today.split('-'))
    days_in_month = days_in_mon(year)
    # Defining the month and day when the the user gives the last date of a month and if we add days to it, the date need to go to the next month.
    # In that case, the day resets to 1 and the month increase by one, if not, then the only the day changes.
    next_day = day + 1
    next_month = month
    next_year = year
    # If the date given by the user is the last day of the year, the date need to go to the next year.
    # If this is the case, then the month resets to 1 and the year increases by 1, if not, then the year remains unchanged.
    if next_day > days_in_month[month]:
        next_day = 1
        next_month += 1
        if next_month > 12:
            next_month = 1
            next_year += 1
    
    # Combines the final output date into DD-MM-YY format
    next_date = f"{next_day:02d}-{next_month:02d}-{next_year}"
    return next_date

def before(today):
    "Accepts a date in the DD-MM-YYYY format and returns the output"
    "as the previous day in the same format."
    # Checking th validity of the date.
    valid, error = valid_date(today)
    if not valid:
        return error
    # Splitting the date given by the user into year,month and day using the map function.
    day, month, year = map(int, today.split('-'))
    days_in_month = days_in_mon(year)
    # If the previous date lies in the same month, the month and year stay the same but the day decreses by 1.
    prev_day = day - 1
    prev_month = month
    prev_year = year
    # If the previous date lies in the previous year, the month resets to 12 and the year decreases by 1 
    # and the day changes to the maximum number of days in the previous month.
    if prev_day < 1:
        prev_month -= 1
        if prev_month < 1:
            prev_month = 12
            prev_year -= 1
        prev_day = days_in_month[prev_month]
    # Combines the final output date into DD-MM-YY format
    prev_date = f"{prev_day:02d}-{prev_month:02d}-{prev_year}"
    return prev_date

def dbda(start_date, num_days):
    "Accepts a date in the DD-MM-YYYY format and returns the output"
    "by calculating the final date."
    # Checking th validity of the date.
    valid, error = valid_date(start_date)
    if not valid:
        return error
    # Enters loop where it calculates the next date by taking the start date as the current date for both after and before function.
    # Making sure to take the absolute value of the argument in order for the correct calculation.
    if num_days >= 0:
        for _ in range(num_days):
            start_date = after(start_date)

    else:
        for _ in range(abs(num_days)):
            start_date = before(start_date)
    
    return start_date

def main():
    "Defines command line arguments."
    # Checks the length of the given date in order to check for error.
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
    # Accept the command line arguments(date and number of days)
    start_date = sys.argv[1]
    num_days = int(sys.argv[2])
    # Define the final output date
    end_date = dbda(start_date, num_days)
    print(end_date)

if __name__ == '__main__':
    main()

