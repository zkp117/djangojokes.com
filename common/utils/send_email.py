import sendgrid
from sendgrid.helpers.mail import Mail
import os

def send_email(to, subject, content):
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    
    email = Mail(
        from_email="pandoraparigian@gmail.com",
        to_emails=to,
        subject=subject,
        html_content=content
    )
    
    response = sg.send(email)
    return response.status_code
