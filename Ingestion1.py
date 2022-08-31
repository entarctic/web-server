from flask import Flask
from flask import request
import requests
import threading 

app = Flask(__name__) #Just naming the app
GOOGLE_SCRIPT_URL = "https://docs.google.com/spreadsheets/d/1Z4GN0kPfH9XtNd9NwLdDdBgKs4PCGFBkccPMvU_bE9E/edit#gid=0"

def send_request_to_gscript(headers,json_data):
	print(f"Sending to script:\nHeaders: {headers} \nJson: {json_data}") #everytime a json data is sent from UnaConnect, will print this line
	requests.post(GOOGLE_SCRIPT_URL, headers=headers, json=json_data) #JSON data will come from UnaConnect
	
@app.route("/sensordata", methods=["POST"])
def sensor_data():
	print(f"Got requests: {repr(request)}") 
	json_data = None #Initialise to None
	try: #to test for errors 
		json_data = request.json #receiving the json data
	except Exception as e: #to handle the error
		print("Exception with sending request to google server")
		print(e)
	return "Success!\n"

if __name__ == "__main__":
	app.run() #(ssl_context = 'adhoc')