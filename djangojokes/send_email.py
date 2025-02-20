import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key="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")
from_email = Email("pandoraparigian@gmail.com")
to_email = To("pandoraparigian@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
print(mail.get())