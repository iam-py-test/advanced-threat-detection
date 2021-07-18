import requests
from hashlib import sha256
from bs4 import BeautifulSoup
badsha256s = requests.get('https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/malware_sig.txt').text.split("\n")
badresponse = requests.get('https://raw.githubusercontent.com/iam-py-test/advanced-threat-detection/main/mal-site.txt').text.split("\n")
domain = input("Enter a domain to scan: ")
req = requests.get('http://{}/sitemap.xml'.format(domain))
xml = req.text
#print(xml)
# https://stackoverflow.com/questions/31276001/parse-xml-sitemap-with-python#31276152
soup = BeautifulSoup(xml,'lxml')
sitemapTags = soup.find_all("url")
xmlDict = {}
for sitemap in sitemapTags:
    try:
        xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text
    except:
        pass
print(xmlDict)
if xmlDict == {}:
    print("No sitemap. Using homepage links...")
    try:
        xmlDict = {}
        reqM = requests.get('http://{}'.format(domain))
        links = BeautifulSoup(xml,'html.parser').find_all("a")
        for link in links:
            xmlDict[link.get("href")] = 'mal'
    except:
        pass

for url in xmlDict:
    req2 = requests.get(url)
    if sha256(req2.content).hexdigest() in badsha256s or sha256(req2.content).hexdigest() in badresponse:
        print("Malware detected on url {}".format(url))
    else:
        print("Url {} clean".format(url))
 
