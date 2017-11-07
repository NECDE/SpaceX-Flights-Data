import requests
import json
import sys

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

def lastflight():
	
	response = requests.get("https://api.spacexdata.com/v1/launches/latest")
	payload = response.json() # list

	if payload:
		for i in payload:
			print('\n-----------------------------------------\n')
			print("\nLast Flight SpaceX\n")
			print("Flight Number: ",i['flight_number'])
			print("Launch Year: ",i['launch_year'])
			print("Launch Date Unix: ",i['launch_date_unix'])
			print("Launch Date (UTC)",i['launch_date_utc'])
			print("Launch Date (LOCAL)",i['launch_date_local'])
			print("Rocket ID: ",i['rocket']['rocket_id'])
			print("Rocket Name: ",i['rocket']['rocket_name'])
			print("Rocket Type: ",i['rocket']['rocket_type'])
			print("Payload: ",i['payloads'][0]['payload_id']," of ",i['payloads'][0]['customers'])
			print("Payload Type: ",i['payloads'][0]['payload_type'])
			print("Orbit: ",i['payloads'][0]['orbit'])
			print("\nDetails: ",i['details'])
			print("\nLaunch ID: ",i['launch_site']['site_id'])
			print("Launch Site: ",i['launch_site']['site_name'])
			print("Launch Success:",i['launch_success'])
			print("Land success:",i['land_success'])
			print("Landing Type: ",i['landing_type'])
			print("landing_vehicle", i['landing_vehicle'])
			print("\nMission Patch: \n",i['links']['mission_patch'])
			print("\nReddit Campaign: \n",i['links']['reddit_campaign'])
			print("\nReddit Launch: \n",i['links']['reddit_launch'])
			print("\nReddit Recovery: \n",i['links']['reddit_recovery'])
			print("\nReddit Media: \n",i['links']['reddit_media'])
			print("\nPresskit: \n",i['links']['presskit'])
			print("\nArticle Link: \n",i['links']['article_link'])
			print("\nVideo Link: \n",i['links']['video_link'])
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

if len(sys.argv) >= 2:
	if sys.argv[1] == '-info' or sys.argv[1] == '-i':
		infospacex()
	elif sys.argv[1] == '-last' or sys.argv[1] == '-l':
		lastflight()
	elif sys.argv[1] == '-upcoming' or sys.argv[1] == '-u':
		upcomingflight()
else:
	print("""Usage: python spacex.py [OPTION]

Options:

-i, -info          Company Info
-l, -lastflight    Get latest launch
-u, -upcoming      Get data on upcoming launches
""")
