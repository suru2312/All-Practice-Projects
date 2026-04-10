import pandas as pd
import random
import smtplib
import datetime as dt

MY_EMAIL = "suraj7492sharma@gmail.com"
MY_PASSWORD = "wpbk cvmf tezy rvuk"

now = dt.datetime.now()
today = (now.month, now.day)
birthdays_data = pd.read_csv(r"birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]) : data_row for (index, data_row) in birthdays_data.iterrows()
}

if (today[0], today[1]) in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_path = rf"letter_templates\letter_{random.randint(1,3)}.txt"
    
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", f"{birthday_person["name"]}")
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = birthday_person["email"],
            msg = f"Subject: Happy Birthday!\n\n{contents}"
        )