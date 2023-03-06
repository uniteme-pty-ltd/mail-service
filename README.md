# mail-service
Microservice that leverages the [Gmail API](https://developers.google.com/gmail/api/guides/sending) to send emails programmatically.

This requires a Service Account to be setup in GCP with Domain-wide delegation enabled. See [here](https://developers.google.com/gmail/api/guides/sending#delegate_domain-wide_authority_to_your_service_account) for more details.

## Getting Started

1. Copy the GCP Service Account's credentials file (`sa_creds.json`) into the root directory of the project. You can find this in LastPass.

2. Ensure the environment variables are set correctly in `docker-compose.yaml`.

3. Start the development server
```bash
docker compose up
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
