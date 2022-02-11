# 딕셔너리는 aaa = { } 안을 말한다.

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "berlin"
}

# 딕셔너리안에 리스트를 만든다
travel_log = {
    "France": ["paris", "Lille", "Dijion"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# 딕셔너리 안에 딕셔너리를 중첩해본다.

travel_log = {
    "France": {"cities_visited": ["paris", "Lille", "Dijion"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# 이제 리스트 안에 딕셔너리를 중첩해본다.
# 여러개의 키-값 쌍으로 이루어진 하나의 큰 딕셔너리 대신에 각각의 항목들이 각각의 딕셔너리가 되도록 바꿀것이다.
# 다시말해 "France"라는 키의 값인 딕셔너리 대신에 이 값도 키-값 쌍으로 바꿀것이다.
# "country"라는 키를 만들고 이 안에 "France"를 값으로 넣는다.
# 이제 세 데이터가 모두 들어간 하나의 딕셔너리가 만들어졌다 1 방문한나라, 2 도시, 3 방문횟수
travel_log = [ # []대괄호로 바꿔주면 이제 원하는 만큼의 딕셔너리들을 이 리스트 안에 추가 할수 있다.
    {
     "country": "France", # 첫번재 값은 문자열이고
     "cities_visited": ["paris", "Lille", "Dijion"], # 두 번째 값은 리스트이고
     "total_visits": 12 # 세번재 값은 정수이다.
     },
    {
     "country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
     },
]


