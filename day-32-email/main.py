import smtplib
import datetime as dt
import random

my_email = "atlasov.aial@gmail.com"
password = input("Whats your password")
subject = "Monday motivation"
message = f"Hi! \nHope you doing well! I sent this message via Python\nBest Regards,\n{my_email}"


now = dt.datetime.now()
weekday = now.weekday()
# 0-monday, 1-tuesday, 3-wednesday etc
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    # print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ayal227@yahoo.com",
            msg=f"Subject:{subject}\n\n" f"{quote}"
        )

