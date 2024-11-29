from datetime import date,datetime
import calendar
today = date.today()
now = datetime.now()

print("The date is:", today)
print("\nThe time is:", now)

print("\nDate components", today.year, today.month, today.day)
date1 = date(2025,7,22) 
date2 = date(2025,12,8)

print("Diffrence between date 1 and date 2 is:", (date2 - date1))
time1 = datetime(2024,11,29,6,30,0) 
time2 = datetime(2024,11,29,8,19,56)

print("Diffrence between time 1 and time 2 is:", (time2 - time1))
#calendar#
print("--------------------")

print(calendar.calendar(2025))

print(calendar.month(2026, 12))