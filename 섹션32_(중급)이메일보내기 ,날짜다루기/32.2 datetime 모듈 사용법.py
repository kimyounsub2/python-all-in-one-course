import datetime as dt

now = dt.datetime.now() # 현재의 날짜와 시각을 알려주게 된다.
year = now.year
minth = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year = 1993, month = 3, day =30, hour = 4)
print(date_of_birth)