import time
import datetime

#time in Long format
print(time.time())

"""
Y: year
m: month
d: day
H: hour
M: minutes
S: seconds
//Defined formats
c: local date time
X: hours:minutes:seconds
x: day/month/year
"""

# Time in hours:minutes:seconds
print(time.strftime("%H:%M:%S"))
# Date in day/month/year
print(time.strftime("%d/%m/%Y"))

print(time.strftime("%c"))
print(time.strftime("%x"))

now = datetime.datetime.now()
print(now)
print(now.minute)
print(now.month)
print(datetime.date.today().year)
date = "01/12/1999"
#we send the text format NOT the wanted format
date = datetime.datetime.strptime(date,"%d/%m/%Y")
print(date)

date = date + datetime.timedelta(days = 3, weeks=1, hours = 1)
print(date)

now2 = datetime.datetime.now()+ datetime.timedelta(hours = 1)
future2HNow = now+datetime.timedelta(hours = 2)
if now2<future2HNow:
	delta = future2HNow - now2
	#For delta we can only use days, seconds or microseconds
	print("more than hour, access token expired by "+ str(delta.seconds) + "sec")