# with open("weather_data.csv") as data_file:
#     data = data_file.readlines() # weather_data 파일 안에 있는 각 줄을 가져다가 리스트에 들어갈 요소로 바꾸기 위해서
#     print(data)
    
# 파이썬은 실제로 데이터 처리와 데이터 분석에 아주 많이 사용되기 때문에 CSV를 지원하는 내장 라이브러리가 있다.
# 날씨 데이터처럼 표형태로 된 데이터를 다루기 위한 도구들이 많이 잇다.

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
    
# 위에 내용처럼 온도만 리스트로 가져오기 위해서는 코드가 복잡해지지만 판다스를 이용하면 편하다

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

    

 