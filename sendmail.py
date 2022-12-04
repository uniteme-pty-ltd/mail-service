import services

import base64
from email.message import EmailMessage
from googleapiclient.errors import HttpError


def send_email(recipient, subject, message_content):

	message = EmailMessage()
	message['To'] = recipient
	message['From'] = 'UniteMe <admin@uniteme.app>' # Changing the email here doesn't seem to be portrayed on the email that is sent. Need to investigate.
	message['Subject'] = subject

	# Plain text emails
	# message.set_content(message_content)

	# HTML emails
	message.add_header('Content-Type','text/html')
	message.set_payload(message_content)

	

	# Encode the entire message (headers, content and all) as a base64 string
	encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
	# print(message.as_bytes())

	# Create a message body to send to the API
	create_message = {
		'raw': encoded_message
	}

	try:
		# Send the message (via Cloud service client library defined in services.py)
		send_message = (services.gmail_service.users().messages().send(
			userId='me', # Indicates the authenticated user. To my understanding, this could be a literal email address if the Service Account has permission to use it, but I can't get it to work..
			body=create_message
		).execute())
		print(F'Email "{subject}" sent to "{recipient}". Message ID: {send_message["id"]}')
	
	except HttpError as error:
		print(F'An error occurred: {error}')
		send_message = None

	return send_message



send_email('tscott8520@gmail.com', 'This is the subject', 'Message body in <b>html</b> format!')