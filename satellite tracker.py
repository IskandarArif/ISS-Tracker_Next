import json
from urllib import response
import urllib.request
import time
import datetime
from datetime import datetime

# takes inputs for date and time
my_string = str(input('Enter date(yyyy-mm-dd hh:mm:ss): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M:%S")

tuple = my_date.timetuple()
timestamp = time.mktime(tuple)

print(timestamp)


sat_position = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps=" + \
    str(timestamp) + "&units=miles"
response = urllib.request.urlopen(sat_position)
result = json.loads(response.read())


while True:
    latlong = "https://api.wheretheiss.at/v1/satellites/25544"
    response = urllib.request.urlopen(latlong)
    result = json.loads(response.read())
    # print("Satellite: " + str(result["name"]))

    # get the lat and lon
    lat = result["latitude"]
    lon = result["longitude"]
    print(lat, lon)

    # to display where the current location of the satellit
    coordinate = "https://api.wheretheiss.at/v1/coordinates/" + \
        str(lat)+","+str(lon)
    response = urllib.request.urlopen(coordinate)
    location = json.loads(response.read())
    tz_id = location["timezone_id"]
    offset = location["offset"]
    cc = location["country_code"]

    # if the country code returns "??" then satellite is not over an+y country
    if cc == "??":
        cc = "None"

    print("Time zone is: " + str(tz_id) + "\nOffset: " +
          str(offset) + "\nCountry code: " + str(cc))

    time.sleep(5)
