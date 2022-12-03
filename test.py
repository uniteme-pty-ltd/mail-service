from google.oauth2 import service_account
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file(
	filename='sa_creds.json',
	scopes=['https://mail.google.com/'],
	subject='admin@uniteme.app'
)

service_gmail = build('gmail', 'v1', credentials=creds)
response = service_gmail.users().getProfile(userId='me').execute()
print(response)