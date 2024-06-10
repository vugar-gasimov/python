import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "getostur@gmail.com"
my_password = "demedimgetostur"

# letter_1 = r"day32\birthday-wisher-hard-start\letter_templates\letter_1.txt"
# letter_2 = r"day32\birthday-wisher-hard-start\letter_templates\letter_2.txt"
# letter_3 = r"day32\birthday-wisher-hard-start\letter_templates\letter_3.txt"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
# all_letters = [letter_1, letter_2, letter_3]
# random_letter = random.choice(all_letters)
df = pd.read_csv(r"day32\birthday-wisher-hard-start\birthdays.csv")

# Create a dictionary with (month, day) as keys and rows as values
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# birthdays_dict = {(data_row["month"], data_row.day): data_row for (index, data_row) in df.iterrows()} 
birthdays_dict = {}
for index, row in df.iterrows():
    month_day_tuple = (row["month"], row["day"])
    birthdays_dict[month_day_tuple] = row
    persons_name = (row["name"])
    persons_email = (row["email"])
    # print(persons_name, persons_email)
    # print(birthdays_dict)


if today_tuple in birthdays_dict:
    # print("Today is someone's birthday!")
    random_letter = fr"day32\birthday-wisher-hard-start\letter_templates\letter_{random.randint(1, 3)}.txt"
    with open(random_letter) as f:
        r_letter_data = f.read()
    r_letter_data = r_letter_data.replace("[NAME]", persons_name)
    # print(r_letter_data)
    try: 
        with smtplib.SMTP("smtp.gmail.com",) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=persons_email, 
                msg=f"Subject:Happy Birthday!\n\n{r_letter_data}"
                )
            print("Email sent successfully!")
    except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError, smtplib.SMTPException) as e:
        print(f"Failed to send email: {e}")
    except TimeoutError:
        print("A connection attempt failed due to timeout.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
else:
    print("Today is no one's birthday!")