import datetime
from datetime import *

date = input("enter last date: ")
period = int(input("enter time in monnths: "))

formart = "%Y/%m/%d %H:%M:%S"
dat = datetime.strptime(date, formart)
day = dat.date()

i = 0
while i <= period:
	if i <= period:
		
		print(day + timedelta(28 * period))
		i += 1

	else:
		quit()
