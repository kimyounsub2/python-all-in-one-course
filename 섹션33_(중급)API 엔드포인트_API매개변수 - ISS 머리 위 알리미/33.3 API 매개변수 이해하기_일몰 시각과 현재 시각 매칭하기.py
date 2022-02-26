import requests
from datetime import datetime

# 실제 홈페이지에서 런던 위도 경도 가져온것
MY_LAT = 51.507351
MY_LONG = -0.127758

# 이제 lat키를 상수인 MY_LAT으로 설정하고 lng키는 MY_LONG으로 설정한다.
# 여기 API 문서에 지정된 키들을 이용해서 그걸 모두 딕셔너리로(parameters)로 형식화 한것

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0, # 유닉스 타임으로 변경해준다. 6:52:08 AM -> 2022-02-25T06:52:08+00:00
}

# 이 딕셔너리를(parameters) requests.get 의 params인자 안에 넣으면

reponse = requests.get("https://api.sunrise-sunset.org/json" ,params=parameters )
reponse.raise_for_status()
data = reponse.json()
# 출력되는 내용에서 sunrise, sunset내용만 출력할수 있다.
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")) # split("T")를 추가하면 2022-02-25T06:52:08+00:00 -> ['2022-02-25', '06:52:08+00:00']
print(sunrise.split("T")[1].split(":")) # [1].split(":")를 추가하면 ['2022-02-25', '06:52:08+00:00'] -> ['06', '52', '08+00', '00']
print(sunrise.split("T")[1].split(":")[0]) # [0]를 추가하면  ['06', '52', '08+00', '00'] 여기서 0번째 문자이 06만 출력된다.

########### 이렇게 해서 원하는 마지막 시간을 출력할수 있다.
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

# 오류건 테슽

time_now = datetime.now()
