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
#π¨ Do NOT change the code above

#TODO: Write the function that will allow new countries
def add_new_country(country_visited, times_visited, cities_visited):
    new_country ={}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country) # append() ν¨μλ λ¦¬μ€νΈ ννμ Dataμ λ§μ§λ§μ νλλ₯Ό μΆκ°νλ ν¨μ

#to be added to the travel_log. π
add_new_country("νκ΅­",2,["μμΈ","λΆμ°"])
print(travel_log)