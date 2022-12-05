# mail-service
Microservice that leverages the [Gmail API](https://developers.google.com/gmail/api/guides/sending) to send emails programmatically.

This requires a Service Account to be setup in GCP with Domain-wide delegation enabled. See [here](https://developers.google.com/gmail/api/guides/sending#delegate_domain-wide_authority_to_your_service_account) for more details.

## Getting Started

Create virtual environemt
```bash
# Note: only necessary on first setup
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
# Note: only necessary on first setup
pip install -r requirements.txt
```

Copy the GCP Service Account's credentials file (`sa_creds.json`) into the root directory of the project. You can find this in LastPass.

Copy `.env.example` to `.env` and fill in the necessary values.
```bash
# Note: only necessary on first setup
cp .env.example .env
vim .env
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
| X-API-KEY | abc123 |

### Request Body

```json
{
	"recipient": string, 		// recipient's email address
	"subject": string, 			// email subject
	"base64_content": string 	// email body (base64 encoded)
}
```

## Deploying

Retrieve the real SECRET_KEY from LastPass and add it to the `.env` file to secure the API.

Will need to be behind an NGINX reverse proxy for security.

> Flask is a WSGI *application*. A WSGI *server* is used to run the *application*, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.
>
> WSGI servers have HTTP servers built-in. However, a dedicated HTTP server may be safer, more efficient, or more capable. Putting an HTTP server in front of the WSGI server is called a “reverse proxy.”
>
> [-- Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/deploying/)
