from services import gmail_service

import base64
from email.message import EmailMessage
from googleapiclient.errors import HttpError


def send_email(sender_name, recipient, subject, base64_message_content):

	# Decode base64-encoded message content.
	# We will re-encode it before sending, but we have to include
	# the headers and everything in the final encoded message we send off.

	# Convert base64_message_content string to bytes
	base64_bytes = base64_message_content.encode('utf-8')
	# Decode the bytes
	raw_bytes = base64.b64decode(base64_bytes)
	# Convert decoded bytes back into raw string
	decoded_message_content = raw_bytes.decode('utf-8')

	message = EmailMessage()
	message['To'] = recipient
	message['From'] = sender_name + ' <admin@uniteme.app>' # Changing the email here doesn't seem to be portrayed on the email that is sent. Need to investigate.
	message['Subject'] = subject

	# Plain text emails
	# message.set_content(decoded_message_content)

	# HTML emails
	message.add_header('Content-Type','text/html')
	message.set_payload(decoded_message_content)

	# Encode the entire message (headers, content and all) as a base64 string
	# Use it to create a message body to send to the API
	create_message = {
		'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
	}

	try:
		# Send the message (via Cloud service client library defined in services.py)
		send_message = (gmail_service.users().messages().send(
			userId='me', # Indicates the authenticated user. To my understanding, this could be a literal email address if the Service Account has permission to use it, but I can't get it to work..
			body=create_message
		).execute())
		print(F'Email "{subject}" sent to "{recipient}". Message ID: {send_message["id"]}')
	
	except HttpError as error:
		print(F'An error occurred: {error}')
		send_message = None

	return send_message
