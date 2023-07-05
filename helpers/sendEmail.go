package helpers

import (
	"crypto/tls"
	"fmt"
	"net/smtp"
	"os"
)

func SendEmailOverSmtp(sender, recipient, subject, body string) error {
	// Set up SMTP authentication credentials
	smtpHost := os.Getenv("SMTP_HOST")
	smtpPort := os.Getenv("SMTP_PORT")
	smtpUsername := os.Getenv("SMTP_USER")
	smtpPassword := os.Getenv("SMTP_PASS")

	// Compose the email message
	message := []byte(
		"Subject: " + subject + "\r\n" +
			"\r\n" +
			body + "\r\n",
	)

	// Set up the SMTP client
	auth := smtp.PlainAuth("", smtpUsername, smtpPassword, smtpHost)

	// Connect to the SMTP server
	conn, err := smtp.Dial(smtpHost + ":" + smtpPort)
	if err != nil {
		return fmt.Errorf("failed to connect to the SMTP server: %v", err)
	}
	defer conn.Close()

	// Initiate STARTTLS negotiation
	tlsConfig := &tls.Config{
		InsecureSkipVerify: true, // Adjust this as per your security requirements
		ServerName:         smtpHost,
	}

	err = conn.StartTLS(tlsConfig)
	if err != nil {
		return fmt.Errorf("failed to start TLS: %v", err)
	}

	// Re-authenticate with the SMTP server after upgrading the connection to TLS
	if err := conn.Auth(auth); err != nil {
		return fmt.Errorf("SMTP authentication failed: %v", err)
	}

	// Set the sender and recipient
	if err := conn.Mail(sender); err != nil {
		return fmt.Errorf("failed to set the sender: %v", err)
	}
	if err := conn.Rcpt(recipient); err != nil {
		return fmt.Errorf("failed to set the recipient: %v", err)
	}

	// Send the email message
	w, err := conn.Data()
	if err != nil {
		return fmt.Errorf("failed to open data writer: %v", err)
	}
	_, err = w.Write(message)
	if err != nil {
		return fmt.Errorf("failed to write email message: %v", err)
	}
	err = w.Close()
	if err != nil {
		return fmt.Errorf("failed to close data writer: %v", err)
	}

	return nil
}
