from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
htmlBytes = page.read()
html = htmlBytes.decode("utf-8")
titleIndex = html.find("<title>")
startIndex = titleIndex + len("<title>")
endIndex = html.find("</title>")
title = html[startIndex:endIndex]
find = re.findall("ab*c", "ABC", re.IGNORECASE)
print(find)