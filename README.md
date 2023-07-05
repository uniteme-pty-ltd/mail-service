# mail-service

Microservice that leverages the AWS SES + SMTP to send emails programmatically.

## Development

1. Install dependencies

```bash
go mod download
```

2. Define environment variables for your development environment:

> These are passed to the Docker container via `docker-compose.yaml` in development. When running in production, the environment variables must be passed to the container when it is run.

```bash
cp .env.example .env
vim .env
```

3. Start the development server

```bash
docker compose up
```

## Deploying to Production

```bash
# Build Docker image for production:
docker build -t mail-service -f Dockerfile.production .

# Example manually running a container with environment variables defined:
docker run -p 8080:8080 -e SMTP_HOST=x SMTP_PORT=x SMTP_USER=x SMTP_PASS=x mail-service
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

| Header       | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

### Request Body

```json
{
	"recipient": string, 		// recipient's email address
	"subject": string, 			// email subject
	"base64_content": string 	// email body (base64 encoded)
}
```
