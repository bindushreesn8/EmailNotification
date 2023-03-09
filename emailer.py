import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("dbcpolarbear@gmail.com", "sdguyoyuvnnqdyhw")

# message to be sent
message = "Hello Surendra Sir, how you are doing??, Have a good Day"

# sending the mail
s.sendmail("dbcpolarbear@gmail.com", "sevaopsb@gmail.com", message)

# terminating the session
s.quit()
