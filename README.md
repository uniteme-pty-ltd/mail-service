# mail-service
Microservice that leverages the [Gmail API](https://developers.google.com/gmail/api/guides/sending) to send emails programmatically.

This requires a Service Account to be setup in GCP with Domain-wide delegation enabled. See [here](https://developers.google.com/gmail/api/guides/sending#delegate_domain-wide_authority_to_your_service_account) for more details.

## Development

1. Copy the GCP Service Account's credentials file (`sa_creds.json`) into the root directory of the project. You can find this in LastPass.

2. Ensure the environment variables are set correctly in `docker-compose.yaml`.

3. Start the development server

> This builds the Docker image and runs it automatically with the config defined in docker-compose.yaml. This saves you having to build the docker image and then run a manual docker run command with all the flags (for environment variables, ports, etc).

```bash
docker compose up
```

## Deploying to Production

Will need to be behind an NGINX reverse proxy for security.

> Flask is a WSGI *application*. A WSGI *server* is used to run the *application*, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.
>
> WSGI servers have HTTP servers built-in. However, a dedicated HTTP server may be safer, more efficient, or more capable. Putting an HTTP server in front of the WSGI server is called a “reverse proxy.”
>
> [-- Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/deploying/)

1. Copy the GCP Service Account's credentials file (`sa_creds.json`) into the root directory of the project. You can find this in LastPass. Yes, this file gets baked into the container. This is a temporary solution until we can figure out a better way to do this, but Google's authentication & auth client libraries are complicated and annoying.

2. Build and run the production image.

```bash
# Build Docker image for production:
docker build -t mail-service-api .

# Example manually running a container with environment variables and ports defined:
docker run -p 8080:80 -e SA_CREDS_LOCATION=sa_creds.json mail-service-api
```

## API Contract

### Health check

```
GET /
```

### Send Email
```
POST /v1/send
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
