# mail-service
Microservice that leverages the [Gmail API](https://developers.google.com/gmail/api/guides/sending) to send emails programmatically.

## Getting Started

Create virtual environemt
```bash
# Note: only necessary after first cloning the repo
python3 -m venv venv
```


Activate virtual environment
```bash
# MacOS & Linux
. venv/bin/activate

# Windows Powershell
venv\Scripts\activate
```

Install dependencies within virtual environment
```bash
# Note: only necessary after first cloning the repo
pip install -r requirements.txt
```

Start the Flask development server
```bash
flask run
```

Dectivate virtual environment
```bash
deactivate
```

## API Contract

### Send Email
```
POST https://localhost:5000/v1/send
```
### Request headers

| Header | Value |
| - | - |
| Content-Type | application/json |
| X-API-KEY | API KEY |

### Request Body

```json
{
	"recipient": string, 		// recipient's email address
	"subject": string, 			// email subject
	"base64_content": string 	// email body (base64 encoded)
}
```

## Deploying

Will need to be behind an NGINX reverse proxy for security.

> Flask is a WSGI *application*. A WSGI *server* is used to run the *application*, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.
>
> WSGI servers have HTTP servers built-in. However, a dedicated HTTP server may be safer, more efficient, or more capable. Putting an HTTP server in front of the WSGI server is called a “reverse proxy.”
>
> [-- Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/deploying/)
