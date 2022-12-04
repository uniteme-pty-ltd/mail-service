import services

import base64
from email.message import EmailMessage


message = EmailMessage()

message.set_content('This is a draft message.')

message['To'] = 'tscott8520@gmail.com'
message['From'] = 'admin@uniteme.app' # Changing this doesn't seem to affect the email that is sent. Need to investigate.
message['Subject'] = 'Automated draft'

# encoded message
encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

create_message = {
	'raw': encoded_message
}

send_message = (services.gmail_service.users().messages().send(
	userId='me', # Indicates the authenticated user. To my understanding, this could be a literal email address if the Service Account has permissions, but I can't get it to work..
	body=create_message
).execute())

print(F'Email message ID: {send_message["id"]}')