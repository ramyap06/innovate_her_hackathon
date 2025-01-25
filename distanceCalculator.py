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

for i in range(4):
    distance = ((lat[i] - int_latitude) ** 2) + ((long[i] - int_longitude) ** 2)
    if (distance <= 10):
        sites.append([name[i], description[i], lat[i], long[i]])




