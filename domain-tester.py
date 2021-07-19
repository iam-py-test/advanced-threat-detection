import requests
domains = requests.get("https://curben.gitlab.io/malware-filter/urlhaus-filter-domains-online.txt").text.split("\n")
detectionrate = 0
misseddomains = []
testeddomains = 0
for domain in domains:
  if domain.startswith("#"):
    domains.remove(domain)
for domain in domains:
  if domain.startswith("#") or domain == "":
    continue
  testeddomains += 1
  try:
    requests.get(domain)
  except Exception as err:
    detectionrate += 1
    print("{} blocked. {} domains tested. Proactive detection at {}%".format(domain,testeddomains,(detectionrate/len(domains))*100))
  else:
    misseddomains.append(domain)
    print("{} not blocked. {} domains tested. Proactive detection at {}%".format(domain,testeddomains,(detectionrate/len(domains))*100))

pdr = detectionrate/len(domains))*100
print("Test complete. {} domains tested. Final detection at {}".format(len(domains)),pdr))
o = input("Test done. Exit?")
