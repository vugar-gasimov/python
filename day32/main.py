# import smtplib

# my_email= "@gmail.com"
# my_password= ""
# my_second_e = "@gmail.com"

# with smtplib.SMTP("smpt.gmail.com") as connection:

#     #TLS transport layer security

#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     # connection.sendmail(from_addr=my_email, to_addrs=my_second_e, msg="Hello from Python")
#     connection.sendmail(from_addr=my_email, to_addrs=my_second_e, msg="Subject:Hello\n\n This is from Python")
# # connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(now)
# if year == 2024:
#     print("Be careful.")
# print(f"This is year: {year}.")
# month = now.month
# week_day = now.weekday()
# print(month, week_day)
# date_of_birth = dt.datetime(year=1998, month=6, day=7, hour=14)
# print(date_of_birth)

# Challenge project sending motivational emails on mondays

import datetime as dt
import smtplib
import random

my_email="@gmail.com"
my_password = ""
my_second_e = "@gmail.com"

today = dt.datetime.now()
this_week_day = today.weekday()
monday = 0
# print(today)
# print(this_week_day)
# print(monday)
if this_week_day == monday:
    with open("day32\quotes.txt", "r") as f:
        quotes = f.readlines()
        # print(quotes)
        # ['"When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love..."  - Marcus Aurelius\n',...]
    # random_quote = quotes[random.randint(1,102)]
    random_quote = random.choice(quotes)
    try:
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(
                user=my_email, 
                password=my_password)
            connect.sendmail(
                from_addr=my_email, 
                to_addrs=my_email, 
                msg=f"Subject:Monday Motivation Quote. \n\n {random_quote}.")
    except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError, smtplib.SMTPException) as e:
        print(f"Failed to send email: {e}")
    except TimeoutError:
        print("A connection attempt failed due to timeout.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(random_quote) 

else:
    print("Please wait for monday motivation quotes.")