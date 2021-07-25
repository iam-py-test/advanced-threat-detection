import os
backup = {}
timesrestored = 0
def isencrypted(filename):
	# .encrypted & .fun + https://enterprise.comodo.com/ransomware-extension-list.php + https://www.reddit.com/r/sysadmin/comments/46361k/list_of_ransomware_extensions_and_known_ransom/
	ransomexts = ["encrypted","fun","Krab","AZER","zzzzzzzz","f41o1","ppam","mdk4y","GRHAN","tro","pdff","tfude","israbye","obfuscated","cRh8","3P7m","aRpt","eQTz","3RNu","666","777","xcry7684","venom","Cerber2","HakunaMatata","locked","James","MRCR1","RARE1","PEGS1","REVENGE","SUPERCRYPT","TheTrumpLockerf","TheTrumpLockerp","XTBL","encryptedRSA","crjoker","_crypt","LOL!"]
	for ext in ransomexts:
		if filename.lower().endswith("." + ext.lower()):
			return True
	return False

dirtoprotect = input("Enter the dir to protect: ")
for root,dirs,files in os.walk(dirtoprotect):
		for file in files:
			if isencrypted(file):
				print("File {} already encrypted. Not backing up...".format(file))
				continue
			print("Backing up {}".format(file))
			backup[os.path.join(root,file)] = open(os.path.join(root,file),"rb").read()

while True:
	for root,dirs,files in os.walk(dirtoprotect):
		for file in files:
			if isencrypted(file):
				timesrestored += 1
				print("Ransomware detected. Restoring files...")
				for restorefile in backup:
					try:
						with open(restorefile,"wb") as rf:
							rf.write(backup[restorefile])
							rf.close()
						os.remove(os.path.join(root,file))
					except Exception as err:
						pass
				if timesrestored > len(files) + 1:
					print("Warning: Persistant ransomware detected")
					pid = os.fork()
					if pid == 0:
						print("Scanning for ransomware...")
					timesrestored -= 1
