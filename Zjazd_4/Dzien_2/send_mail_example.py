import smtplib

user = "pythonbootcamp"
password = "123!@#qweQWE"

sent_from = "pythonbootcamp@wp.pl"

to = ["jakubzak93@wp.pl"]
subject = "Try this"
body = "To jest treść"

email_txt = f"""
From: {sent_from}
To: {', '.join(to)}
Subject: {subject}

{body}
"""

try:
    server = smtplib.SMTP_SSL("smtp.wp.pl", 456)
    server.ehlo()
    server.login(user, password)
    server.sendmail(sent_from, to, email_txt)
    server.close()

except Exception as e:
    print(e)
    print("Coś poszło źle")