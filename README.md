# mail-service
Microservice that leverages the [Gmail API](https://developers.google.com/gmail/api/guides/sending) to send emails programmatically.

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

## Deploying

Will need to be behind an NGINX reverse proxy for security.

> Flask is a WSGI *application*. A WSGI *server* is used to run the *application*, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.
>
> WSGI servers have HTTP servers built-in. However, a dedicated HTTP server may be safer, more efficient, or more capable. Putting an HTTP server in front of the WSGI server is called a “reverse proxy.”
>
> [-- Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/deploying/)