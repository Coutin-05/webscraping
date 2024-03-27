from urllib.request import urlopen
import re

'''url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
htmlBytes = page.read()
html = htmlBytes.decode("utf-8")
titleIndex = html.find("<title>")
startIndex = titleIndex + len("<title>")
endIndex = html.find("</title>")
title = html[startIndex:endIndex]
find = re.findall("ab*c", "ABC", re.IGNORECASE)
print(find)'''

'''url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
# this method unifies the two variables above, htmlBytes, html in a single line
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
matchResults = re.search(pattern, html, re.IGNORECASE)
title = matchResults.group()
title = re.sub("<.*?>", "", title) #  remove HTML tags

print(title)'''

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

for string in ["Name: ", "Favorite Color:"]:
    stringStartIdx = html.find(string)
    textStartIdx = stringStartIdx +len(string)

    nextHTMLtagOffset = html[textStartIdx:].find("<")
    textEndIdx = textStartIdx + nextHTMLtagOffset

    rawText = html[textStartIdx : textEndIdx]
    cleanText = rawText.strip(" \r\n\t")
    print(cleanText)
    print(textStartIdx)
    print(textEndIdx)