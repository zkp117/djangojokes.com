import sendgrid
from sendgrid.helpers.mail import Mail
import os

def send_email(to, subject, content):
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

    if not SENDGRID_API_KEY:
        raise ValueError("SendGrid API Key is missing! Check your environment variables.")

    print("Using SendGrid API Key:", SENDGRID_API_KEY[:5] + "*****")

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    
    email = Mail(
        from_email="pandoraparigian@gmail.com", 
        subject=subject,
        html_content=content
    )

    response = sg.send(email)
    print("SendGrid Response:", response.status_code)
    return response.status_code
