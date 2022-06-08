# 외장 라이브러리
# sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

# OS : 환경 변수나 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해준다.
import os
os.environ

# os.chdir : 현재 디렉터리 위치를 변경할 수 있다.
os.chdir("파일경로")

# os.getcwd : 현재 자신의 디렉터리 위치를 돌려준다.

# os.system : 시스템 명령어 호출

# os.popen : 실행한 시스템 명령어의 결괏값 돌려받기

# pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

# shutil : 파일을 복사해 주는 파이썬 모듈
import shutil
shutil.copy("src.txt","dst.txt")

# glob : 특정 디렉터리에 있는 파일 이름 모두를 알아야 할때가 있다.
import glob
glob.golb("파일 경로") 

# time : 시관과 관련된 time 모듈 다양하게 있다.

# time.time : 현재 시간을 실수 형태로 돌려주는 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 돌려준다.

# time.localtime : time.time이 돌려준 실수 값을 사용하여 연도,월,일,시,분,초의 형태로 바꾸어 주는 함수

# time.sleep 일정한 시간 간격을 두고 루프를 실행할수 있다.
import time
for i in range(10):
    print(i)
    time.sleep(1)

# calender : 파이썬에서 달력을 볼수 있게 해준다.
# random : 규칙이 없는 임의수를 발생시킨다.
# random.shuffle : 리스트의 항목을 무작위로 섞고 싶을 때
