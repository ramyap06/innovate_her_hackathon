import ipinfo
import LocationDatabase

access_token = "a0a64e2001c43d"
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()
location = details.loc

latitude = location[0:location.index(",")]
longitude = location[location.index(",")+1:]

int_latitude = float(latitude)
int_longitude = float(longitude)

print(int_latitude + int_longitude)

sites = []

for i in range(8):
    distance = ((LocationDatabase.lat[i] - int_latitude) ** 2) + ((LocationDatabase.long[i] - int_longitude) ** 2)
    if (distance <= 10):
        sites.append([LocationDatabase.name[i], LocationDatabase.description[i], LocationDatabase.lat[i], LocationDatabase.long[i]])




