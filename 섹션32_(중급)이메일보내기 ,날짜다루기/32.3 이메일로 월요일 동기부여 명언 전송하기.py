from importlib.resources import contents
import smtplib
import datetime as dt
import random

MY_EMAIL = "gpgp0330@gamil.com"
MY_PASSWORD = "rladbstjq2@"
 
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice()
    
    print(quote)
    with smtplib.SMTP("smtp.mail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )