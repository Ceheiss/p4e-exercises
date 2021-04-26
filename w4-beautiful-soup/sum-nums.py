import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1213108.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all span tags
tags = soup('span')
numbers = []
count = 0
for tag in tags:
    count = count + 1
    numbers.append(int(tag.contents[0]))

print("Count", count)
print("Sum", sum(numbers))