import sendgrid
import os
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
message = Mail(
    from_email="pandoraparigian@gmail.com",
    to_emails="pandoraparigian@gmail.com",
    subject="Test Email",
    plain_text_content="This is a test email from SendGrid."
)

try:
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
