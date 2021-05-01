import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Set up file connection
url = input("Enter location:")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_1213110.xml"

def get_data(url):
  # Get the XML data decoded
  print("Retrieving", url)
  data = urllib.request.urlopen(url).read().decode()
  print("Retrieved", len(data), "characters")
  return data

def find_instances(data, param):
  tree = ET.fromstring(data)
  lst = tree.findall(param)
  print("Count: ", len(lst))
  return lst

def add_nums(lst):
  result = 0
  for item in lst:
    result = result + int(item.text)
  return result

result = add_nums(find_instances(get_data(url),'.//count'))
print("Sum:", result)


# The program will prompt for a URL
# read the XML data from that URL using urllib
# then parse and extract the comment counts from the XML data
# compute the sum of the numbers in the file.