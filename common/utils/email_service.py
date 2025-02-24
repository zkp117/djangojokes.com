import sendgrid
from sendgrid.helpers.mail import Mail
import os

def send_email(to, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY')) 
    email = Mail(
        from_email='pandoraparigian@gmail.com',
        to_emails=to,
        subject=subject,
        plain_text_content=content
    )
    response = sg.send(email)
    return response
