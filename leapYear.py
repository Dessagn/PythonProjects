__author__ = 'Temesgen'

# Determine if a year is a leap year.


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif yr % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print "Enter a year you want to check"
yr = int(raw_input(">_ "))
year = is_leap_year(yr)
if year:
    print "The year %r is a leap year." % yr
else:
    print "The year %r is not a leap year." % yr
