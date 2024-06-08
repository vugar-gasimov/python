
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import pandas as pd
import datetime as dt

today = dt.datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv(r"day32\birthday-wisher-hard-start\birthdays.csv")

# Create a dictionary with (month, day) as keys and rows as values
birthdays_dict = {}
for index, row in df.iterrows():
    month_day_tuple = (row["month"], row["day"])
    birthdays_dict[month_day_tuple] = row
    print(birthdays_dict)


if today_tuple in birthdays_dict:
    print("Today is someone's birthday!")
else:
    print("Today is no one's birthday!")