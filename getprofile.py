import services

response = services.gmail_service.users().getProfile(userId='me').execute()
print(response)