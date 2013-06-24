# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	elapsed = 0
	dy = year2 - year1
	dm = month2 - month1
	dd = day2 - day1
	print dy, dm, dd
	
	bump_year = False
	bump_month = False        
	
	return elapsed

# Test routine

def test():
	test_cases = [((2012,1,1,2012,2,28), 58), 
				  ((2012,1,1,2012,3,1), 60),
				  ((2011,6,30,2012,6,30), 366),
				  ((2011,1,1,2012,8,8), 585 ),
				  ((1900,1,1,1999,12,31), 36523)]
	for (args, answer) in test_cases:
		result = daysBetweenDates(*args)
		if result != answer:
			print "Test with data:", args, "failed"
		else:
			print "Test case passed!"

test()

