import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_url(url, position, times):
  new_url = ""
  last_name = ""
  # We use the url retrieved to do the new search
  for time in range(times):
    if (len(new_url) != 0):
      url = new_url
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all anchor tags
    tags = soup('a')
    counter = 0
    for tag in tags:
      link = re.findall(r'http.*html',str(tag))[0]
      if (counter == position - 1):
        new_url = link
        last_name = tag.contents[0]
      counter = counter + 1
  return '"' + last_name + '"'



print("The answer to the assignment for this execution is", get_url("http://py4e-data.dr-chuck.net/known_by_Aden.html", 18, 7))

# get line at position
# parse the line to extract the url
# print that is retrieving it
# use the new url as argument and run the project again (count amount of times)
# return the value