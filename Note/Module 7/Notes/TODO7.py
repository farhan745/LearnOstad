import datetime

current = datetime.datetime.now()

print(current.year)
print(current.month)
print(current.hour)
print(current.time())
print(current.second)
print(current.microsecond)
print(current.weekday())

format_current=current.strftime("%d/%m/%Y")
print(format_current)


date1 = datetime.datetime(1991,12,9)
date2 = datetime.datetime(2024,9,30)
diff = date2-date1
print(diff)

add10DaysWithDay1 = date1 + datetime.timedelta(days=5)
print(add10DaysWithDay1)