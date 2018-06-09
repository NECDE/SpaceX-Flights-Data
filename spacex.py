import requests
import sys

def inforecycl(link):

	response = requests.get(link)
	payload = response.json()

	def info_print():
		print('\n-----------------------------------------\n')
		print("\nLast Flight SpaceX\n")
		print("Flight Number: ",payload['flight_number'])
		print("Mission name: ",payload['mission_name'])
		print("Launch Year: ",payload['launch_year'])
		print("Launch Date Unix: ",payload['launch_date_unix'])
		print("Launch Date (UTC)",payload['launch_date_utc'])
		print("Launch Date (LOCAL)",payload['launch_date_local'])
		print("Telemetry link: ",payload['telemetry']['flight_club'])

		# ROCKET DETAILS
		print("Rocket ID: ",payload['rocket']['rocket_id'])
		print("Rocket Name: ",payload['rocket']['rocket_name'])
		print("Rocket Type: ",payload['rocket']['rocket_type'])
		print("Payload: ",payload['rocket']['second_stage']['payloads'][0]['payload_id'],"of")
		lalas=0
		for i in payload['rocket']['second_stage']['payloads'][0]['customers']:
			lalas=+1
			print(i)
			if lalas>1:
				print(" and ")
		print("Payload Type: ",payload['rocket']['second_stage']['payloads'][0]['payload_type'])
		print("Orbit: ",payload['rocket']['second_stage']['payloads'][0]['orbit'])
		print("Land success:",payload['rocket']['first_stage']['cores'][0]['land_success'])
		print("Landing Type: ",payload['rocket']['first_stage']['cores'][0]['landing_type'])
		print("landing vehicle",payload['rocket']['first_stage']['cores'][0]['landing_vehicle'])

		print("\nDetails: ",payload['details'])

		# LAUNCH SITE
		print("\nLaunch ID: ",payload['launch_site']['site_id'])
		print("Launch Site: ",payload['launch_site']['site_name'])
		print("Launch Site: ",payload['launch_site']['site_name_long'])

		print("Launch Success:",payload['launch_success'])

		# LINKS
		print("\nMission Patch: \n",payload['links']['mission_patch'])
		print("\nMission Patch: \n",payload['links']['mission_patch_small'])
		print("\nReddit Campaign: \n",payload['links']['reddit_campaign'])
		print("\nReddit Launch: \n",payload['links']['reddit_launch'])
		print("\nReddit Recovery: \n",payload['links']['reddit_recovery'])
		print("\nReddit Media: \n",payload['links']['reddit_media'])
		print("\nPresskit: \n",payload['links']['presskit'])
		print("\nArticle Link: \n",payload['links']['article_link'])
		print("\nArticle Link: \n",payload['links']['wikipedia'])
		print("\nVideo Link: \n",payload['links']['video_link'])
		print('\n-----------------------------------------\n')

	if len(payload) < 10:
		for payload in payload:
			info_print()
	else:
		info_print()

def infospacex():
	response = requests.get("https://api.spacexdata.com/v2/info")
	payload = response.json()

	print('\n-----------------------------------------\n')
	print("\nSpaceX Info\n")
	print("Name: ",payload['name'])
	print("Founder: ",payload['founder'])
	print("Founded: ",payload["founded"])
	print("Employees: ",payload['employees'])
	print("Vehicles: ",payload['vehicles'])
	print("Launch sites: ",payload['launch_sites'])
	print("Test sites: ",payload['test_sites'])
	print("CEO: ",payload['ceo'])
	print("CTO: ",payload['cto'])
	print("COO: ",payload['coo'])
	print("CTO Propulsion: ",payload['cto_propulsion'])
	print("Valuation: ",payload['valuation'])
	print("Headquarters: ",payload['headquarters']['address']+", "+payload['headquarters']['city']+", "+payload['headquarters']['state'])
	print("\nSummary: ",payload['summary'])

def falconheavy():

	response = requests.get("https://api.spacexdata.com/v2/rockets/falconheavy")
	payload = response.json()

	print('\n-----------------------------------------\n')
	print("\nFalcon Heavy stats\n")
	print("Name: ",payload['name'])
	print("Type: ",payload['type'])
	print("Active: ",payload['active'])
	print("Stages: ",payload['stages'])
	print("Boosters: ",payload['boosters'])
	print("Cost per launch: ",payload['cost_per_launch'])
	print("Success rate pct: ",payload['success_rate_pct'])
	print("First flight: ",payload['first_flight'])
	print("Country: ",payload['country'])
	print("Company: ",payload['company'])

	print("Height: ",payload['height']["meters"],"meters")
	print("Diameter: ",payload['diameter']["meters"],"meters")
	print("Mass: ",payload['mass']["kg"])

	for h in range(len(payload["payload_weights"])):
		print("\nName:",payload["payload_weights"][h]["name"])
		print("Kg:",payload["payload_weights"][h]["kg"])

	# print("Meters: ",payload['height']["meters"])
	# print("Meters: ",payload['height']["meters"])
	# print("Meters: ",payload['height']["meters"])
	# print("Meters: ",payload['height']["meters"])
	print("\nDescription: ",payload['description'])


if len(sys.argv) >= 2:
	if sys.argv[1] == '-info' or sys.argv[1] == '-i' or sys.argv[1] == 'i':
		infospacex()

	elif sys.argv[1] == '-last' or sys.argv[1] == '-l' or sys.argv[1] == 'l':
		inforecycl("https://api.spacexdata.com/v2/launches/latest")

	elif sys.argv[1] == '-upcoming' or sys.argv[1] == '-u' or sys.argv[1] == 'u':
		inforecycl("https://api.spacexdata.com/v2/launches/upcoming")

	elif sys.argv[1] == '-next' or sys.argv[1] == '-n' or sys.argv[1] == 'n':
		inforecycl("https://api.spacexdata.com/v2/launches/next")

	elif sys.argv[1] == '-heavy' or sys.argv[1] == '-h' or sys.argv[1] == 'h':
		falconheavy()

else:
	print("""Usage: python spacex.py [OPTION]

Options:

-i, -info          Company Info
-l, -lastflight    Get latest launch data
-n, -next          Get next launch data
-u, -upcoming      Get upcoming launches data
-h, -heavy         Get Falcon Heavy data
""")
