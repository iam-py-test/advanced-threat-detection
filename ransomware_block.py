import os
backup = {}
timesrestored = 0
def isencrypted(filename):
	ransomexts = ["encrypted"]
	for ext in ransomexts:
		if filename.endswith("." + ext):
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
					timesrestored -= 1
