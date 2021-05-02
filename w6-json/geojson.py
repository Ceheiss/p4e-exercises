# Should work like this:
#  $ python3 solution.py
#  Enter location: South Federal University
#  Retrieving http://...
#  Retrieved 2458 characters
#  Place id ChIJ0V94rPl_bIcR6KyIGL16ZQ:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
# Early exit
if len(address) < 1:
  print("Goodbye")
  exit()

# Pass API params as a dictionary to make the request
# Ends up like: http://py4e-data.dr-chuck.net/json?address=santiago&key=42
params = {'address': address, 'key': api_key}
url = serviceurl + urllib.parse.urlencode(params)

# Retrieve data from the API
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(data), 'characters')

# Exit if something goes wrong getting the JSON
try:
  json_data = json.loads(data)
except:
  json_data = None

if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
  print('Something went wrong, could not retrieve data')
  exit()

# Get and print place idjson_data
place_id = json_data["results"][0]["place_id"]
print("Place id", place_id)
