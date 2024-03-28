from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

baseUrl = "https://www.xcmg-america.com/"

htmlPage = urlopen(baseUrl)
htmlText = htmlPage.read().decode("utf-8")
soup = BeautifulSoup(htmlText, "html.parser")
for link in soup.find_all("a"):
    linkUrl =  link["href"]
    print(linkUrl)