import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
data_dict = data.to_dict() # data를 딕셔너리 유형으로 바꿀것이다.
print(data_dict)# 각 열에 독립된 딕셔너리를 만들기 위해 판다스가 표와 표에 있는 열을 가져간 것을 볼수 있다

tem_list = data["temp"].to_list() # 이 data 시리즈는 파이썬 리스트로 바뀐다.
print(len(tem_list))

average = sum(tem_list) / len(tem_list)
print(average)

print(data["temp"].mean()) # 위에 계산식이 없이도 평균을 구할수 있다.
print(data["temp"].max()) # 온도에서 최댓값을 구할수 있다.

# 데이타의 열을 찾는다
print(data["condition"])
print(data.condition) # []대괄호 없이도 .을 이용해 같은 열을 출력할수 있다.

#데이터의 줄을 찾는다
print(data[data.day == "Monday"]) # day의 컬럼을 찾고 monday의 줄을 찾는다
print(data[data.temp == data.temp.max()]) # temp의 온도를 찾고 온도가 최댓값의 줄을 찾는다.

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp) # monday_temp라는 변수에 monday.temp 값을 찍고 그값을 정수로 변환
monday.temp_F = monday_temp * 9/5 +32 # 섭씨를 화씨로 구하는 공식
print(monday.temp_F)


############### 처음부터 데이터 프레임을 만드는 방법
data_dict ={
    "students": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data) # 딕셔너리(data_dict)의 갓을 사용해서 표가 만들어진것을 볼수 있다.
data.to_csv("new_data.csv") # 엑셀시트로 변환할수 있다.




# 판다스의 두 가지 주요 데이터 구조인 시리즈(series)와 데이터 프레임(dataframe)이 있다.

#데이터 프레임(dataframe)
#전체 표와 같은 것이라고 보면된다. 엑셀파일이나 구글시트에 있는 각각의 시트들은 판다스에서 데이터 프레임으로 간주한다.

#시리즈(series)
#기본적으로 리스트와 같은 것이다. 표에서 한 열과 같은 것인데 말하자면 온도열과 같은거다

#전체 표는 기본적으로 판다스에서 데이터 프레임이고 모든 각각의 개별 열들의 리스트는 시리즈이다.
