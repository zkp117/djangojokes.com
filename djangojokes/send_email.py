import ssl
import certifi
import sendgrid
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient(api_key="YOUR_API_KEY")
message = Mail(
    from_email="pandoraparigian@gmail.com",
    to_emails="pandoraparigian@gmail.com",
    subject="Test Email",
    plain_text_content="Hello from DjangoJokes!"
)

# Create an SSL context that uses the correct certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Send email with SSL context
response = sg.client.mail.send.post(request_body=message.get(), ssl_context=ssl_context)
print(response.status_code)
