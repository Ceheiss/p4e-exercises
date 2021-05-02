import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Set up file connection
url = input("Enter location:")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_1213111.json"
print("Retrieving", url)

# Get data
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")
# Get data as JSON
json_data = json.loads(data)
# print(json.dumps(json_data, indent=2))  --> To get data in a pretty way

comments_list = json_data["comments"]
print("Count:", len(comments_list))
total_number = 0

for comment in comments_list:
  total_number = total_number + int(comment["count"])

print("Sum:", total_number)