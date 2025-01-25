import requests
import googlemaps

# ipinfo_url = "https://ipinfo.io/json?token=4cc93606f30bd1"
#response = requests.get(ipinfo_url)
#location_data = response.json()

#user_lat = location_data["loc"].split(",")[0]
#user_lon = location_data["loc"].split(",")[1]

# Replace with your API Key from Google Cloud
API_KEY = "AIzaSyCMq3bpKoGR6S3QDRyZqq7Y2szxfebmP4w"
gmaps = googlemaps.Client(key=API_KEY)

# Use Google Maps Geolocation API
result = gmaps.geolocate()

# Print the location result (Latitude & Longitude)
print("Your current location:")
print("Latitude:", result['location']['lat'])
print("Longitude:", result['location']['lng'])
