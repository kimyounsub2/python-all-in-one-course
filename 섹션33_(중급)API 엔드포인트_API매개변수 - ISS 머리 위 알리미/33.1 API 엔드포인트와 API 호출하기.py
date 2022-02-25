
import requests

response = requests.get(url= "http://api.open-notify.org/iss-now.json")
print(response) # 200이 출력되는데 문제가 없을때이다.

############### 오류코드정리
# 100 : Hold on 잠시만요 뭔가 진행되고 있고 아직 최종이 아니라는 의미
# 200 : Here You Go 그건 여기 있습니다. 모든게 잘되었고 기대하신 데이터를 받을 것이라는 의미
# 300 : Go Away 그건 보통 여러분이 이걸 받을 권한이 없으니까 그냥 가라는 의미
# 400 : You Screwed Up 여러분이 잘못 되었다는 의미이다. 404가 될수도 있고 존재하지 않는다는 말이다.
# 500 : I Screwed Up 여러분이 요청을 한 서버가 잘못 되었다는 의미이다. 서버가 다운되었거나 웹사이트가 다운되었거나 혹은 다른 이슈가 있을때

response = requests.get(url= "http://api.open-notify.org/is75652-now.json")
if response.status_code != 200: # 주소가 틀려 404에러가 출력된다. 
    print("Error")
    
response = requests.get(url= "http://api.open-notify.org/is75652-now.json")
response.raise_for_status() # 이렇게 해주면 오류코드와 함께 오류내용을 알수가 있다.

response = requests.get(url= "http://api.open-notify.org/iss-now.json")
data = response.json() # 사이트에 있는 내용들이 출력된다.

data_iss = response.json()["iss_position"] # 사이트 내용중에 일부만 출력시킬수 있다.
data_iss_position = response.json()["iss_position"]["longitude"]
print(data)
print(data_iss)
print(data_iss_position)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position =(longitude,latitude)
print(iss_position)