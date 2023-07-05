package handlers

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func HealthCheck(c *gin.Context) {

	smtpHost := os.Getenv("SMTP_HOST")
	smtpPort := os.Getenv("SMTP_PORT")
	smtpUsername := os.Getenv("SMTP_USER")
	smtpPassword := os.Getenv("SMTP_PASS")

	if smtpHost == "" || smtpPort == "" || smtpUsername == "" || smtpPassword == "" {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": "Missing environment variables",
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"healthy": true,
	})
}
