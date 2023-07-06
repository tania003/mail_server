import smtplib

sender_email = 'sender mail'
password = 'password'
recevier_email = 'receiver mail'
message = 'This is SMTP.mail_server. Mail sent .' 

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email,password)
s.sendmail(sender_email,recevier_email,message)
s.quit()

print("Email sent successfully!")