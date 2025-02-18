const email= require('@sendgrid/mail');

/* User Can Set the SendGrid's API Key Here */
email.setApiKey('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');

/* User Can Set the Email Content Here */
const emailContent= {
  to: 'pandoraparigian@gmail.com',
  from: 'pandoraparigian@gmail.com',
  subject: 'Sending an email using SendGrid',
  text: 'Hello from SendGrid!',
};

/* User Can Send the Email By Using send method*/
email.send(emailContent)
  .then(() => {
    console.log('Email sent successfully');
  })
  .catch((error) => {
    console.error('Error sending email:', error);
  });