from datetime import datetime,timedelta
import time

time1 = datetime.now().time()
time.sleep(1)
time2 = datetime.now().time()

print(time1)
print(time2)
# diff between these 2 times
print(type(time1))
print(type(time2))