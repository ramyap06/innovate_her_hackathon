import ipinfo
import LocationDatabase

access_token = "a0a64e2001c43d"
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()
location = details.loc

latitude = location[0:location.index(",")]
longitude = location[location.index(",")]

int_latitude = int(latitude)
int_longitude = int(longitude)

print(int_latitude + int_longitude)

