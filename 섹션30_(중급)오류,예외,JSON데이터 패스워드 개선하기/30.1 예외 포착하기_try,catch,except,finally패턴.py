# FileNotFound 예외를 살펴보고 그리고 그 예외를 잡아서 이걸 훨씬 안전하게 만든느 방법을 알아보자

# a_file 없기 때문에 이 코드 오류를 유발할수 이는 코드라인이다.
# 그래서 이 코드 라인은 try 블록 안에 들어간다.
try: # 우리가 시도해 볼 코드라인이 된다.
    file = open("test.txt")
except:
    print("There was an error") # 위에 코드가 파일이 없어 오류가 발생했고 따라서 except가 실행된거다

# try, except, else, finally 이 네가지 키워드는 오류를 처리하고 예외를 잡을때 가장 중요하다.    
try: 
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w") #위에 코드가 오류가 나지만 except에서 실행된 코드는 문제가 없어 파일이 생성된것을 볼수있다.
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    print("File was closed. ")
    
# raise 키워드를 사용하면 자신만의 예외를 생성할수 있다.
    
height = float(input("Height: "))
weight = int(input("Weight: "))

# 만약 입력자가 해당범위를 넘어서는 값을 입력했을때 
# ValueError은 오류가 발생했고 오류메세지를 출력할수 있다.
if height > 3:
    raise ValueError("Human Heigh should not be over 3 meters. ")

bmi = weight / height**2
print(bmi)