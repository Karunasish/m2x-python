#!/usr/bin/env python

# Usage:
#   $ API_KEY=<YOUR MASTER API KEY> python example.py

import os

from m2x.client import M2XClient
from m2x.v2.devices import Device
 
client = M2XClient(key=os.environ['API_KEY'])

params = {
	"visibility": "private",
	"status": "enabled",
	"limit": "3"
}

response = Device.search(api = client, params = params)
if len(response) > 0:
    print("\nDevice Details :")
    for device in response:
        print("Device name: %s Device Id: %s Device Visibility: %s Device Status: %s " % (device.name, device.id, device.visibility, device.status ))
else:
    print("Devices not available in this search criteria")
 