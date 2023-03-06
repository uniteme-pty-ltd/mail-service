# Handle authentication and the creation of required API clients ("services")

from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

SA_CREDS_LOCATION = os.getenv("SA_CREDS_LOCATION")

creds = service_account.Credentials.from_service_account_file(
    filename=SA_CREDS_LOCATION,
    scopes=['https://mail.google.com/'],
    subject='admin@uniteme.app'
)

# Create authenticated Gmail API client
gmail_service = build('gmail', 'v1', credentials=creds)


# creds_delegated = creds.with_subject('no-reply@uniteme.app')
# gmail_service = build('gmail', 'v1', credentials=creds_delegated)
# Returns {'error': 'invalid_grant', 'error_description': 'Invalid email or User ID'}
