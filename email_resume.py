from email_validator import validate_email, EmailNotValidError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def _load_secrets():
    with open("secrets.txt", 'r') as f:
        secrets = f.readlines()

    secrets_dict = {}

    for line in secrets:
        key, val = line.split(':')
        val = val.replace('\n', '')
        secrets_dict[key] = val

    return secrets_dict

def _is_valid(email_address):
    try:
        valid = validate_email(email_address)
        return True

    except EmailNotValidError as e:
        return False

def email_resume(email_address):
    if _is_valid(email_address):
        mail_content = "TEST EMAIL"

        secrets_dict = _load_secrets()
        username = secrets_dict['gmail_address']
        password = secrets_dict['gmail_pw']

        message = MIMEMultipart()
        message['From'] = username
        message['To'] = email_address
        message['Subject'] = "Mike Kane's Resume"

        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('64.233.184.108', 587)
        session.starttls()
        session.login(username, password)
        text = message.as_string()
        session.sendmail(username, email_address, text)
        session.quit()
        print('mail sent')
    else:
        print("Invalid Email Address!")


