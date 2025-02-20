import sendgrid
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient(api_key="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")  # Replace with actual key or use os.getenv()
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