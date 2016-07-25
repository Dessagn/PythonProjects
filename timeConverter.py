__author__ = 'Temesgen'

"""
This program will convert the number of seconds or minutes and change it to
number of hours and minutes in 12hrs format or 24hrs format.
"""

def seconds_to_12hrs(sec):
    hrs = sec / 3600
    hrs_remainder = sec % 3600
    minutes = hrs_remainder / 60
    minutes_remainder = hrs_remainder % 60
    seconds = minutes_remainder
    return "%r hours, %r minutes and %r seconds" % (hrs, minutes, seconds)

def minutes_to_12hrs(min):
    hrs = min / 60
    hrs_remainder = min % 60
    return "%r hours and %r minutes." % (hrs, hrs_remainder)

time = seconds_to_12hrs(100000)
print time


