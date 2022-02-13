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

# function to get the position of satellite every 10 minutes before the initial timestamp for an hour


def pos_before(timestamp):
    for x in range(6):

        sat_position = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps=" + \
            str(timestamp) + "&units=miles"
        response = urllib.request.urlopen(sat_position)
        result = json.loads(response.read())
        lat = result[0]["latitude"]
        lon = result[0]["longitude"]

        # to display where the current location of the satellit
        coordinate = "https://api.wheretheiss.at/v1/coordinates/" + \
            str(lat)+","+str(lon)
        response = urllib.request.urlopen(coordinate)
        location = json.loads(response.read())
        tz_id = location["timezone_id"]
        offset = location["offset"]
        cc = location["country_code"]
        actual_time = datetime.fromtimestamp(timestamp)

        # if the country code returns "??" then satellite is not over an+y country
        if cc == "??":
            cc = "None"

        print("\nLatitude and Longitde: " + str(lat) + "," + str(lon) + "\nTime and date: " + str(actual_time) + "\nTime zone is: " + str(tz_id) + "\nOffset: " +
              str(offset) + "\nCountry code: " + str(cc))

        time.sleep(1)
        timestamp = (timestamp - 600)


# function to get the position of satellite every 10 minutes after the initial timestamp for an hour
def pos_after(timestamp):
    for x in range(6):

        sat_position = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps=" + \
            str(timestamp) + "&units=miles"
        response = urllib.request.urlopen(sat_position)
        result = json.loads(response.read())
        lat = result[0]["latitude"]
        lon = result[0]["longitude"]

        # to display where the current location of the satellit
        coordinate = "https://api.wheretheiss.at/v1/coordinates/" + \
            str(lat)+","+str(lon)
        response = urllib.request.urlopen(coordinate)
        location = json.loads(response.read())
        tz_id = location["timezone_id"]
        offset = location["offset"]
        cc = location["country_code"]
        actual_time = datetime.fromtimestamp(timestamp)

        # if the country code returns "??" then satellite is not over an+y country
        if cc == "??":
            cc = "None"

        print("\nLatitude and Longitde: " + str(lat) + "," + str(lon) + "\nTime and date: " + str(actual_time) + "\nTime zone is: " + str(tz_id) + "\nOffset: " +
              str(offset) + "\nCountry code: " + str(cc))

        time.sleep(1)

        timestamp = (timestamp + 600)


pos_before(timestamp)
pos_after(timestamp)
