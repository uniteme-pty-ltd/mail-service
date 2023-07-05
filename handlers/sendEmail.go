package handlers

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/uniteme-pty-ltd/mail-service/helpers"
)

func SendEmail(c *gin.Context) {

	sender := "admin@uniteme.app"
	recipient := "admin@uniteme.app"
	subject := "Test Email"
	body := "This is a test email sent using SMTP with STARTTLS."

	err := helpers.SendEmailOverSmtp(sender, recipient, subject, body)
	if err != nil {
		fmt.Println("Error sending email:", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"success": false,
			"message": "Error sending email, see server logs for more details.",
		})
		return
	}

	fmt.Println("Email sent successfully!")
	c.JSON(http.StatusNoContent, gin.H{
		"success": true,
		"message": "Email sent successfully!",
	})
}
