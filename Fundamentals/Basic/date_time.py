from datetime import datetime, date, timedelta

# #obj
# d = date(2019, 4, 19)
# print(d)

# d1 = datetime.today()
# print(d1)

# #priority
# now = datetime.now()
# print(now)

# print(now.timestamp())

'''Convert string to datetime and oposite'''
# d = datetime.strptime('19-04-2019','%d-%m-%y')
# print(d)


# d1 = datetime(2019, 4, 19)
# d2 = datetime(2019, 12, 31)

# duration = d2 - d1 
# print(duration.days, duration.seconds)


now = datetime.now()
print(now.day, now.month, now.hour, now.minute, now.second, now.weekday())