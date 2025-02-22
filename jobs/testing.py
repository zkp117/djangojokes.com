import sendgrid
from sendgrid.helpers.mail import Mail

api_key = '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'  # Replace with your SendGrid API key

sg = sendgrid.SendGridAPIClient(api_key)

# Create a test email (you can use any email here, it's just for testing)
from_email = 'pandoraparigian@gmail.com'  # Replace with your email
to_email = 'pandoraparigian@gmail.com'  # Replace with any valid email

email = Mail(from_email, 'Test Subject', to_email, 'Test Body')

# Send the email (you don't need to send it to the recipient, just making a request to test)
try:
    response = sg.send(email)
    print(f"Response Code: {response.status_code}")
    print(f"Response Body: {response.body}")
    print(f"Response Headers: {response.headers}")
except Exception as e:
    print(f"Error: {e}")