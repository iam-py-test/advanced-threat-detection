try:
  import requests
except:
  import subprocess
  subprocess.run("pip3 install requests",shell=True)
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
    requests.get("http://{}".format(domain))
  except Exception as err:
    detectionrate += 1
    print("{} blocked. {} domains tested. Proactive detection at {}%".format(domain,testeddomains,(detectionrate/len(domains))*100))
  else:
    misseddomains.append(domain)
    print("{} not blocked. {} domains tested. Proactive detection at {}%".format(domain,testeddomains,(detectionrate/len(domains))*100))

pdr = (detectionrate/len(domains))*100
print("\n\n")
for domain in misseddomains:
  print("Domain missed: {}".format(domain))
print("Test complete. {} domains tested. {} missed domains. Final detection at {}".format(len(domains),len(misseddomains),pdr))
o = input("Test done. Exit?")
