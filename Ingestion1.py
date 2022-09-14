from flask import Flask
from flask import request
import requests
import threading 

app = Flask(__name__) #Just naming the app
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxOLBarWGWFDp1TBS_2D-7YlM0vzPBHDi0wp4igdfAtjUgI4anBoGg5CkFx_4gyLQM/exec"


def send_request_to_gscript(headers,json_data):
	print(f"Sending to script:\nHeaders: {headers} \nJson: {json_data}") #everytime a json data is sent from UnaConnect, will print this line
	#requests.post(GOOGLE_SCRIPT_URL, headers=headers, json=json_data) #JSON data will come from UnaConnect
	requests.post(	"https://entarctic-web-server.herokuapp.com/", headers=headers, json=json_data) #JSON data will come from UnaConnect
	
@app.route("/sensordata", methods=["POST"])
def sensor_data():
	print(f"Got requests: {repr(request)}") 
	json_data = None #Initialise to None
	try: #to test for errors 
		json_data = request.json #receiving the json data
	except Exception as e:
		print("Exception with parsing json data")
		print(e)
	headers = request.headers
	try:
		t = threading.Thread(target=send_request_to_gscript, args= (headers, json_data))
		t.start()
	except Exception as e: #to handle the error
		print("Exception with sending request to google server")
		print(e)
	return "Success!\n"

if __name__ == "__main__":
	app.run() #(ssl_context = 'adhoc')
