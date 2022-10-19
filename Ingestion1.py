from flask import Flask
from flask import request
import requests
import threading 

from http.client import HTTPConnection
import logging                                                                                                                                                
HTTPConnection.debuglevel = 1 
log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)

app = Flask(__name__) #Just naming the app
GOOGLE_SCRIPT_TEMPERATURE_URL = "https://script.google.com/macros/s/AKfycbxkQoIrqm9zer8YbllV7PhSc2-DX_gqBgpUWjZI4Pb_qJom5gNUAkolYmO9v6lnowUeDA/exec"
GOOGLE_SCRIPT_POWER_URL = "https://script.google.com/macros/s/AKfycbyYLvJ1BlTbndFYszpeXWUbOdSOgqZ6SwBhHfL186M4rtUfTmRNZcjRZaSYroZNgb2yXg/exec"
GOOGLE_SCRIPT_FLEXSENSE_URL = "https://script.google.com/macros/s/AKfycbz5cfHu08J2SvVcOTLKnfaSII7XTU45GciKzNozrDPQMoRD63OSMr1k5L38jzOZFH8n/exec"


def send_request_to_gscript1(headers,json_data1):
	print(f"Sending to script:\nHeaders: {headers} \nJson: {json_data1}") #everytime a json data is sent from UnaConnect, will print this line
	requests.post(GOOGLE_SCRIPT_TEMPERATURE_URL, json=json_data1) #JSON data will come from UnaConnect
	#requests.post(	"https://entarctic-web-server.herokuapp.com/", headers=headers, json=json_data) #JSON data will come from UnaConnect
def send_request_to_gscript2(headers,json_data2):
	print(f"Sending to script:\nHeaders: {headers} \nJson: {json_data2}") #everytime a json data is sent from UnaConnect, will print this line
	requests.post(GOOGLE_SCRIPT_POWER_URL, json=json_data2) #JSON data will come from UnaConnect
	#requests.post(	"https://entarctic-web-server.herokuapp.com/", headers=headers, json=json_data) #JSON data will come from UnaConnect
def send_request_to_gscript3(headers,json_data3):
	print(f"Sending to script:\nHeaders: {headers} \nJson: {json_data3}") #everytime a json data is sent from UnaConnect, will print this line
	requests.post(GOOGLE_SCRIPT_FLEXSENSE_URL, json=json_data3) #JSON data will come from UnaConnect
	#requests.post(	"https://entarctic-web-server.herokuapp.com/", headers=headers, json=json_data) #JSON data will come from UnaConnect
	
@app.route("/temperaturedata", methods=["POST"])
def temperature_data():
	print(f"Got requests: {repr(request)}") 
	json_data1 = None #Initialise to None
	try: #to test for errors 
		json_data1 = request.json #receiving the json data
	except Exception as e:
		print("Exception with parsing json data")
		print(e)
	headers = request.headers
	try:
		t = threading.Thread(target=send_request_to_gscript1, args= (headers, json_data1))
		t.start()
	except Exception as e: #to handle the error
		print("Exception with sending request to google server")
		print(e)
	return "Success!\n"

@app.route("/powerdata", methods = ["POST"])
def power_data():
	print(f"Got requests: {repr(request)}") 
	json_data2 = None #Initialise to None
	try: #to test for errors 
		json_data2 = request.json #receiving the json data
	except Exception as e:
		print("Exception with parsing json data")
		print(e)
	headers = request.headers
	try:
		t = threading.Thread(target=send_request_to_gscript2, args= (headers, json_data2))
		t.start()
	except Exception as e: #to handle the error
		print("Exception with sending request to google server")
		print(e)
	return "Success!\n"

@app.route("/humiditydata", methods = ["POST"])
def humidity_data():
	print(f"Got requests: {repr(request)}") 
	json_data3 = None #Initialise to None
	try: #to test for errors 
		json_data3 = request.json #receiving the json data
	except Exception as e:
		print("Exception with parsing json data")
		print(e)
	headers = request.headers
	try:
		t = threading.Thread(target=send_request_to_gscript3, args= (headers, json_data3))
		t.start()
	except Exception as e: #to handle the error
		print("Exception with sending request to google server")
		print(e)
	return "Success!\n"


if __name__ == "__main__":
	app.run() #(ssl_context = 'adhoc')
