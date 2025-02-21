from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "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"  # Replace with your real key

message = Mail(
    from_email="pandoraparigian@gmail.com",
    to_emails="pandoraparigian@gmail.com",
    subject="SendGrid Test Email",
    html_content="<h1>Test</h1><p>Checking API Key</p>"
)

try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print("Status Code:", response.status_code)
    print("Response Body:", response.body)
except Exception as e:
    print("Error:", e)
