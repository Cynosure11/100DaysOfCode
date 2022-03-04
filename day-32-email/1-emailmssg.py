import smtplib

# input("Whats your e-mail?")
my_email = "atlasov.aial@gmail.com"
password = input("Whats your password")
subject = input("What is subject?")
message = f"Hi! \nHope you doing well! I sent this message via Python\nBest Regards,\n{my_email}"


# smtp is different for any mails. check google like icloud smtp
with smtplib.SMTP("smtp.gmail.com") as connection:
    # start tls = Transport Layer Security
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="ayal227@yahoo.com",
        msg=f"Subject:{subject}\n\n" f"{message}"
    )











