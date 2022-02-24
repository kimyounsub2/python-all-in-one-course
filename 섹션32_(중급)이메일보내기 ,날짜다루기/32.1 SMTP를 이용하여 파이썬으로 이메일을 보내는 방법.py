from multiprocessing import connection
import smtplib

my_email = "gpgp0330@gmail.com" # 자신의 이메일 입력
# @앞에 있는 부분은 이메일 계정의 신원에 해당하고 @ 뒤에 있는 부분은 이메일 제공자의 신원에 해당한다.
password = "rladbstjq2@"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # 이메일 서버와의 연결을 안전하게 만드는 방식을 말한다.
    # 그렇게 하면 우리가 이메일을 전송할때 만일 다른 누군가가 그 과정의 어딘가에서 이메일을 가로채고 읽으려 한다면, 
    # 이 함수가(starttls) 작동할것이고 메시지가 암호화되어 메일의 내용을 알수 없게 한다.


    ############################## 구글에서 보완설정을 약하게 따로 해줘야 한다.

    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr= my_email , 
        to_addrs="k20121236@gamil.com", 
        msg="Subject:제목을 적는다 \n\n 전달할 메세지를 내용을 입력한다."
        )

#connection.close() # with ~~ as 를 사용하면 닫기를 안해줘도 된다.
# 아이디와 비번이 잘못되면 오류가 발생하니 주의하자


