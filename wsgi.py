from flask import Flask, jsonify, abort, request, make_response
from werkzeug.exceptions import HTTPException
import json
import base64

from sendmail import send_email

# Create an instance of the class
app = Flask(__name__)

@app.route('/v1/send', methods=['POST'])
def v1_send():

	if request.headers.get('X-API-KEY') != 'abc123':
		abort(401)

	# If Content-Type isn't application/json, abort with 415
	if not request.headers.get('Content-Type') or request.headers.get('Content-Type') != 'application/json':
		abort(400, description='Missing required Content-Type header: application/json')

	# request_body = request.get_json()
	request_body = request.json
	if 'recipient' not in request_body.keys():
		abort(400, description='Missing required field: recipient')
	if 'subject' not in request_body.keys():
		abort(400, description='Missing required field: subject')
	if 'base64_content' not in request_body.keys():
		abort(400, description='Missing required field: base64_content')
	

	# TODO: Add error handling for if send_email() fails
	# try:
	# 	send_email(...)
	# except Exception as e:
	# 	abort(500, description=str(e))

	email_details = send_email(
		request_body['recipient'].lower(),
		request_body['subject'],
		request_body['base64_content']
	)

	return make_response(
		jsonify(email_details),
		200,
		{ 'Content-Type': 'application/json' }
	)



# Ensure HTTP errors are returned as JSON

@app.errorhandler(HTTPException)
def handle_exception(error):
	# Start with the correct headers and status code from the error
	response = error.get_response()
	# Replace the body with JSON
	response.data = json.dumps({
		"code": error.code,
		"name": error.name,
		"description": error.description,
	})
	# Set the content type header to idicate JSON
	response.content_type = "application/json"
	return response
