from urllib import response
import requests
# from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# API키를 잡아야 한다. appid
api_ked ="69f04e4613056b159c2761a9d9e664d2" 
account_sid = "AC7c35~~~" # Twilio사이트에서 키값받아서 입력
autn_token = "03240dfa3df234"
weather_params = {
    "Lat": 51.507351,  #위도 런던의 위도 사이트에서 조회
    "Lon": -0.127758, # 경도
    "appid" : api_ked,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params) 
response.raise_for_status()
weather_data = response.json()
weather_slice =weather_data["hourly"][:12] # 이미 다음 12시간의 모든 날씨 상태로 된 리스트를 얻었다

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"] # 다음 12시간을 반복시켜서 각각의 시간에 대한 날씨상태 id를 잡앗다.
    if int(condition_code) < 700: # 날씨 홈페이지에서 비가오는 날이 700이하 이다.
        will_rain = True

# if will_rain:
#     # SMS 문자 정송 코드
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#             body ="Join Earth's mightiest heroes. Like Kevin Bacon.",
#             from = " +0222222",
#             to = "0222222"
#         )
# print(message.status)