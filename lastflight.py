import requests
import json

response = requests.get("https://api.spacexdata.com/v1/launches/latest")

payload = response.json() # list

lastflight = payload[0] # dict

flight_number = lastflight['flight_number'] # int
launch_year = lastflight['launch_year'] # str
launch_date_utc = lastflight['launch_date_utc'] # str
launch_date_local = lastflight['launch_date_local'] # str

rocket = lastflight['rocket'] # dict
rocket_id = rocket['rocket_id'] # str
rocket_name = rocket['rocket_name'] # str
rocket_type = rocket['rocket_type'] # str

telemetry = lastflight['telemetry'] # dict
flight_club = telemetry['flight_club'] # NoneType

core_serial = lastflight['core_serial'] # str
cap_serial = lastflight['cap_serial'] # NoneType

reuse = lastflight['reuse'] # dict
core = reuse['core'] # bool
side_core1 = reuse['side_core1'] # bool
side_core2 = reuse['side_core2'] # bool
fairings = reuse['fairings'] # bool
capsule = reuse['capsule'] # bool

launch_site = lastflight['launch_site'] # dict
site_id = launch_site['site_id'] # str
site_name = launch_site['site_name'] # str

payloads = lastflight['payloads'] # list
payloaden = payloads[0] # dict
payload_id = payloaden['payload_id'] # str
customers = payloaden['customers'] # list
payload_type = payloaden['payload_type'] # str
payload_mass_kg = payloaden['payload_mass_kg'] # int
payload_mass_lbs = payloaden['payload_mass_lbs'] # float
orbit = payloaden['orbit'] # str

launch_success = lastflight['launch_success'] # bool
reused = lastflight['reused'] # bool
land_success = lastflight['land_success'] # bool
landing_type = lastflight['landing_type'] # str
landing_vehicle = lastflight['landing_vehicle'] # str

links = lastflight['links'] # dict
mission_patch = links['mission_patch'] # str
reddit_campaign = links['reddit_campaign'] # str
reddit_launch = links['reddit_launch'] # str
reddit_recovery = links['reddit_recovery'] # NoneType 
reddit_media = links['reddit_media'] # str
presskit = links['presskit'] # str
article_link = links['article_link'] # NoneType
video_link = links['video_link'] # str

details = lastflight['details'] # str

print("\nLast Flight SpaceX\n")
print("Flight Number: ",flight_number)
print("Rocket Name: ",rocket_name)
print("Payload: ",payload_id," of ",customers)
print("Payload Type: ",payload_type)
print("\nDetails: ",details)
print("\nLaunch Site: ",site_name)
print("Launch Success:",launch_success)
print("Landing Type: ",landing_type)
print("landing_vehicle", landing_vehicle)
print("Land success:",land_success)
print("Video link: ",video_link)
