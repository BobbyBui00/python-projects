import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./index.html').read_text())
email = EmailMessage()
email['From'] = 'allan.khoabui@gmail.com'
email['To'] = 'allan.khoabui@gmail.com'
email['Subject'] = 'You won a million dollars!'

email.set_content('I am a Python master')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('allan.khoabui@gmail.com', 'zpdx mmiv wrbi obts')
    email.set_content(html.substitute({'name': 'Allan'}), 'html')
    smtp.send_message(email)
    print('Email sent.')