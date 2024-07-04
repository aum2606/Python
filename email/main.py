import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "xyx@email.com"
PASSWORD = "xxxxxxxxxxxxxx"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
birthdays = pd.read_csv("birthdays.csv")
birthday_dict = {(birthday_row["month"], birthday_row["day"]): birthday_row for (index, birthday_row) in birthdays.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letters_file:
        letter = letters_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject: Happy Birthday! \n\n {letter}"
            )



