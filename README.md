# mail-service
Microservice that utilises the [Gmail API](https://developers.google.com/gmail/api/guides/sending) to handle sending emails.

## Getting Started

Create virtual environemt
```bash
python3 -m venv venv
```
> Note: only necessary after first cloning the repo

Activate virtual environment
```bash
# MacOS & Linux
. venv/bin/activate

# Windows Powershell
venv\Scripts\activate
```

Install dependencies within virtual environment
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib Flask
```
> Note: only necessary after first cloning the repo

Start the Flask development server
```bash
flask run
```