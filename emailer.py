import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("dbcpolarbear@gmail.com", "sdguyoyuvnnqdyhw")

# message to be sent
message = "Hello Harsha Sir, how you are doing??, Have a good Sleep"

# sending the mail
s.sendmail("dbcpolarbear@gmail.com", "hemanthkumar.edcs@gmail.com", message)

# terminating the session
s.quit()
