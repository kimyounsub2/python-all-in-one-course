travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
def add_new_country(country_visited, times_visited, cities_visited):
    new_country ={}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country) # append() 함수는 리스트 형태의 Data에 마지막에 하나를 추가하는 함수

#to be added to the travel_log. 👇
add_new_country("한국",2,["서울","부산"])
print(travel_log)