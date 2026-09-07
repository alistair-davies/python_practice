import numpy as np
import math

#A leap year is a year in the Gregorian calendar that contains 
# an extra day, making it 366 days long instead of the usual 365. 
# This extra day, February 29th, is added to keep the calendar 
# synchronized with the Earth’s revolution around the Sun.

#Rules for leap years: a year is a leap year if it’s divisible by 4, 
# unless it’s also divisible by 100 but not by 400.
#Given Input: year = 2024
#Expected Output: 2024 is a leap year

def check_leap_year(year):
    leap_year = False
    if (year %4 == 0 and year % 100 != 0) or year % 400 ==0:  
        leap_year = True
    
    return leap_year

check_year = [2104, 2026, 1900, 2028, 2024, 2000, 2100, 2400]

for year in check_year:
    print(f" Checking leap year for {year} = {check_leap_year(year)}")