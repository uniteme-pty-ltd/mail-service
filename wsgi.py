from flask import Flask, jsonify, abort, request, make_response
import json

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
	if 'body' not in request_body.keys():
		abort(400, description='Missing required field: body')

	# print(request_body['recipient'])

	body = jsonify({
		'hello': 'world'
	})
	return make_response(body, 200, { 'Content-Type': 'application/json' })
