import os
import sendgrid
from sendgrid.helpers.mail import Mail

# Load API Key from environment variable
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

if not SENDGRID_API_KEY:
    print("Error: SENDGRID_API_KEY is not set.")
    exit(1)

sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

# Create the email
message = Mail(
    from_email="zoeparigian2000@gmail.com",  # Use a verified sender
    to_emails="zoeparigian2000@gmail.com",   # Replace with recipient's email
    subject="Test Email from SendGrid",
    plain_text_content="Hello, this is a test email sent from Python in VS Code using SendGrid!"
)

# Send the email
try:
    response = sg.send(message)
    print(f"✅ Email sent! Status Code: {response.status_code}")
except Exception as e:
    print(f"❌ Error: {str(e)}")
