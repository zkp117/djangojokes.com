import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

# Replace with your actual SendGrid API key
api_key = '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'

# Initialize SendGrid API client
sg = sendgrid.SendGridAPIClient(api_key)

# Define the email components
from_email = Email("pandoraparigian@gmail.com")  # Replace with your email address
to_email = To("pandoraparigian@gmail.com")  # Replace with recipient email address
subject = "Test Subject"
content = Content("text/plain", "This is a test email body.")

# Create the Mail object correctly
email_service = Mail(from_email, subject, to_email, content)

try:
    # Send the email and capture the response
    response = sg.send(email)
    
    # Print the response details
    print(f"Response Code: {response.status_code}")
    print(f"Response Body: {response.body}")
    print(f"Response Headers: {response.headers}")
except Exception as e:
    # Print any errors encountered during the email sending attempt
    print(f"Error: {e}")
