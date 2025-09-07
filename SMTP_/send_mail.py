import smtplib as smtp

sender = ""
passw = ""

# Connect to Gmail SMTP server
obj = smtp.SMTP("smtp.gmail.com", 587)
obj.ehlo()
obj.starttls()

# Login (must be strings, not sets)
obj.login(sender, passw)

# Email content
subject = "Email MSG Automation Using Python"
body = "python email msg sending automation"
message = f"Subject: {subject}\n\n{body}"

# List of receivers
list_address = ["sahilminecraft502@gmail.com", "ghimireishwari63@gmail.com"]

# Send mail
obj.sendmail(sender, list_address, message)
print("Sent successfully")

obj.quit()
