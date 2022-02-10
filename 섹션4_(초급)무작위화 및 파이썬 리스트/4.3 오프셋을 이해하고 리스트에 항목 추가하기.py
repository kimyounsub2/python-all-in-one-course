states_of_Korea =["서울", "인천", "부산", "대구"]

print(states_of_Korea[1]) # 인천이조회되다
print(states_of_Korea[-1]) # 음수로도 조회할수 있다 끝부분 대구가 조회된다

states_of_Korea[1] = "제주도"
print(states_of_Korea) # 두번재 인천을 제주도로 바꿔 전체 리스트로 조회 할수있다.

states_of_Korea.append("윤섭") # append 함수는 하나의 항목을 리스트의 마지막에 추가한다
print(states_of_Korea) # 서울, 인천, 부산, 대구, 윤섭 으로들어간다

states_of_Korea.extend("윤섭","김윤섭") # extend 함수는 여러개의 항목을 리스트의 마지막에 추가한다.
print(states_of_Korea) # 서울, 인천, 부산, 대구, 윤섭, 김윤섭 으로들어간다