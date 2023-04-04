from datetime import date
from email.message import EmailMessage
import smtplib

finals = date(2022, 12, 11)
today = date.today()
days_left = (((finals - today).days) - 1)

sender = 'insert bot account email here'
receiver = open('mail list.txt').readlines()
password = 'insert bot account password here'

reminder = EmailMessage()
if days_left > 1:
    reminder['Subject'] = f'{days_left} days until Finals!'
else:
    reminder['Subject'] = f'{days_left} day until Finals!'
reminder['From'] = sender
reminder['Bcc'] = receiver

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, password)
    server.send_message(reminder)
    server.quit()
