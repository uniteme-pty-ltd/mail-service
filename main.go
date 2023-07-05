package main

import (
	"github.com/gin-gonic/gin"

	"github.com/uniteme-pty-ltd/mail-service/handlers"
)

func main() {
	router := gin.Default()
	router.GET("/", handlers.HealthCheck)
	router.POST("/v1/send", handlers.SendEmail)
	router.Run(":8080")
}
