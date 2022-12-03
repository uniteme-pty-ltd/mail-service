import services

import base64
from email.message import EmailMessage


message = EmailMessage()

message.set_content('This is a draft message.')

message['To'] = 'tscott8520@gmail.com'
message['From'] = 'admin@uniteme.app'
message['Subject'] = 'Automated draft'

# encoded message
encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
	.decode()

create_message = {
	'raw': encoded_message
}

send_message = (services.gmail_service.users().messages().send(
	userId='me',
	body=create_message
).execute())

print(F'Email message ID: {send_message["id"]}')