import googlemaps

API_KEY = "AIzaSyCMq3bpKoGR6S3QDRyZqq7Y2szxfebmP4w"
gmaps = googlemaps.Client(key=API_KEY)
response = gmaps.geolocate()

user_lat = response['location']['lat']
user_lon = response['location']['lng']
