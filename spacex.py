import requests
import json

def lastflight():
	
	response = requests.get("https://api.spacexdata.com/v1/launches/latest")
	payload = response.json() # list

	if payload:
		for i in payload:
			print('\n-----------------------------------------\n')
			print("\nLast Flight SpaceX\n")
			print("Flight Number: ",i['flight_number'])
			print("Launch Date (UTC)",i['launch_date_utc'])
			print("Launch Date (LOCAL)",i['launch_date_local'])
			print("Rocket Name: ",i['rocket']['rocket_name'])
			print("Payload: ",i['payloads'][0]['payload_id']," of ",i['payloads'][0]['customers'])
			print("Payload Type: ",i['payloads'][0]['payload_type'])
			print("Orbit: ",i['payloads'][0]['orbit'])
			print("\nDetails: ",i['details'])
			print("\nLaunch Site: ",i['launch_site']['site_name'])
			print("Launch Success:",i['launch_success'])
			print("Landing Type: ",i['landing_type'])
			print("landing_vehicle", i['landing_vehicle'])
			print("Land success:",i['land_success'])
			print("Video link: ",i['links']['video_link'])
			print('\n-----------------------------------------\n')

def upcomingflight():

	response = requests.get("https://api.spacexdata.com/v1/launches/upcoming")
	payload = response.json() # list

	if payload:
		for i in payload:
			print("\nUpcoming Flight SpaceX\n")
			print("Flight Number: ",i['flight_number'])
			print("Launch UTC Date: ",i['launch_date_utc'])
			print("Launch LOCAL Date: ",i['launch_date_local'])
			print("Rocket Name: ",i['rocket']['rocket_name'])
			print("Payload: ",i['payloads'][0]['payload_id']," of ",i['payloads'][0]['customers'])
			print("Payload Type: ",i['payloads'][0]['payload_type'])
			print("Orbit: ",i['payloads'][0]['orbit'])
			print("\nDetails: ",i['details'])
			print("\nLaunch Site: ",i['launch_site']['site_name'])
			# print("Video link: ",i['links']['video_link'])
			print('\n-----------------------------------------\n')

def infospacex():
	response = requests.get("https://api.spacexdata.com/v1/info")
	payload = response.json() # list

	print('\n-----------------------------------------\n')
	print("\nSpaceX Info\n")
	print("Name: ",payload['name'])
	print("Founder: ",payload['founder'])
	print("Employees: ",payload['employees'])
	print("Vehicles: ",payload['vehicles'])
	print("Launch sites: ",payload['launch_sites'])
	print("Test sites: ",payload['test_sites'])
	print("CEO: ",payload['ceo'])
	print("CTO: ",payload['cto'])
	print("COO: ",payload['coo'])
	print("CTO Propulsion: ",payload['cto_propulsion'])
	print("Valuation: ",payload['valuation'])
	print("Headquarters: ",payload['headquarters'])
	print("Summary: ",payload['summary'])

# lastflight()
# upcomingflight()
# infospacex()