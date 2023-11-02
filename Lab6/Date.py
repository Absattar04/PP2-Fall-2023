#1.Write a Python program to subtract five days from current date.
import datetime
x = datetime.date.today()
y = x+datetime.timedelta(days=5)
print(x)
print(y)
 
#2.Write a Python program to print yesterday, today, tomorrow.
import datetime
a = datetime.date.today()
b = a-datetime.timedelta(days=1)
c = a+datetime.timedelta(days=1)
print("Yesterday:",b)
print("Today:",a)
print("Tomorrow:",c)
 
#3.Write a Python program to drop microseconds from datetime.
import datetime
mc = datetime.datetime.now().replace(microsecond=0)
print(mc)

#4.Write a Python program to calculate two date difference in seconds.
from datetime import datetime
def date_diff_in_Seconds(date2, date1):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2023-10-02 00:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("%d seconds" %(date_diff_in_Seconds(date2, date1)))
