from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

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

api_key = os.getenv("SENDGRID_API_KEY")
if not api_key:
    print("❌ ERROR: SENDGRID_API_KEY is not set!")
else:
    print("✅ API Key loaded correctly!")

# delete when completed