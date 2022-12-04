import services

import base64
from email.message import EmailMessage


def send_email(recipient, subject, message_content):
	message = EmailMessage()

	message['To'] = recipient
	message['From'] = 'UniteMe <admin@uniteme.app>' # Changing the email here doesn't seem to be portrayed on the email that is sent. Need to investigate.
	message['Subject'] = subject
	message.set_content(message_content)

	# encoded message
	encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

	create_message = {
		'raw': encoded_message
	}

	send_message = (services.gmail_service.users().messages().send(
		userId='me', # Indicates the authenticated user. To my understanding, this could be a literal email address if the Service Account has permission to use it, but I can't get it to work..
		body=create_message
	).execute())

	print(F'Email message ID: {send_message["id"]}')

send_email('tscott8520@gmail.com', 'This is the subject', 'This is the email contents')