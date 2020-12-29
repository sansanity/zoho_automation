import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import time
import csv
import random

# Define to/from
sender = 'caleb@pitchspot.co'
sender_title = "Caleb Mah"
recipient = 'weekeat3141592654@gmail.com'

# Create message
message = ""
subject = ""

# Defining digital signature
with open("Digital_Signature.html", "r") as f:
    html = f.read()


# Setting up automation: use dictionaries?
## Keys refer to email addresses, Values refer to the names. This allows for slight customization of the email with basic string slicing
# recipients = {"weekeat3141592654@gmail.com": "Caleb", "calebmahweekeat@gmail.com": "James"}
# email_list = list(recipients)
# name_list = list(recipients.values())

# for x in range(len(recipients)):
#     text = "Good Day" + " " + str(name_list[x]) + " " + "I am from Pitchspot"
#     # msg = MIMEText("Message text", 'plain', 'utf-8')
#     msg = MIMEMultipart("html")
#     msg['Subject'] =  Header("Sent from python", 'utf-8')
#     msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
#     msg['To'] = email_list[x]
#     # Referencing message
#     part1 = MIMEText(text, "plain", "utf-8")
#     # Referencing digital signature
#     part2 = MIMEText(html, "html")
#     msg.attach(part1)
#     msg.attach(part2)
#     # Create server object with SSL option
#     server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
#     # Perform operations via server
#     server.login('caleb@pitchspot.co', 'PitchspotRulez!')
#     server.sendmail(sender, email_list[x], msg.as_string())
#     server.quit()
#     time.sleep(5)


##########################################################################

# CSV implementation
with open("sample_leads_list.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for name, email in reader:
        text = f"Good Day" + " " + str(name) + " " + "I am from Pitchspot" \
               f"A separate ine goes here"


               
        # msg = MIMEText("Message text", 'plain', 'utf-8')
        msg = MIMEMultipart("html")
        msg['Subject'] =  Header("Sent from python", 'utf-8')
        msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
        msg['To'] = email
        # Referencing message
        part1 = MIMEText(text, "plain", "utf-8")
        # Referencing digital signature
        part2 = MIMEText(html, "html")
        msg.attach(part1)
        msg.attach(part2)
        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        # Perform operations via server
        server.login('caleb@pitchspot.co', '#####')
        server.sendmail(sender, email, msg.as_string())
        server.quit()
        time.sleep(random.randint(20, 120))


# Test string slicing for First Name / Last Name using .split()