#!/bin/python3
import sys
import json

print("Station,Time,Used,Free")
for station in sys.argv[1:] :
    data=open(station).read()
    json_data=json.loads(data)
    for time, used, free in json_data["ObservationCollection"]["member"][0]["result"]["DataArray"]["values"]:
        print(station.split(".")[0]+","+time+","+used+","+free)

