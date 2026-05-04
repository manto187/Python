import datetime 
now = datetime.datetime.now()
print(now)

# working with date and time
from datetime import datetime
now = datetime.now()
print(now)
# get only date
print(now.date())
# get only time 
print(now.time())


# creating your own date 

from datetime import datetime
my_date = datetime(2020, 5, 17)
print(my_date)


# formatting date and time
from datetime import datetime
now = datetime.now()

formatted  = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)

# calulating time difference
from datetime import datetime
now = datetime.now()
future = datetime(2026, 12, 31)
difference = future - now
print(difference)
# acessing parts 
print(difference.days)
print(difference.seconds)


