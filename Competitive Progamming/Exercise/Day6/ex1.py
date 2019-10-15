"""
Trong 1 năm có 52 tuần nên thường có 52 ngày chủ nhật. Tuy nhiên một số năm có 53 ngày chủ nhật.
Viết chương trình in ra các năm có 53 ngày chủ nhật trong thế kỉ 21
"""
from datetime import date, timedelta

def get_number_of_sunday(year):
    firstDay = date(year, 1, 1)
    lastDay = date(year, 12, 31)

    firstSundayoffSet = 6 - firstDay.weekday()
    days = (lastDay - firstDay).days - firstSundayoffSet

    return days / 7 + 1

years = [year for year in range(2001, 2101)
        if get_number_of_sunday(year) == 53]

print(years)
