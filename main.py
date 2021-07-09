import requests
from hashlib import sha256
from bs4 import BeautifulSoup
badsha256s = requests.get('https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/malware_sig.txt').text.split("\n")
domain = input("Enter a domain to scan: ")
req = requests.get('http://{}/sitemap.xml'.format(domain))
xml = req.text
# https://stackoverflow.com/questions/31276001/parse-xml-sitemap-with-python#31276152
soup = BeautifulSoup(xml)
sitemapTags = soup.find_all("sitemap")
xmlDict = {}
for sitemap in sitemapTags:
    xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text
print(xmlDict)
