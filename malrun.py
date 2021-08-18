import os
import subprocess
from time import sleep
dir = input("Enter the dir to use:")
totalrun = 0
totalblocked = 0
filesmissed = []
for root,dirs,files in os.walk(dir):
	for file in files:
		try:
			print("Running {}".format(file))
			totalrun += 1
			try:
				devnull = open(os.devnull, 'wb')
				subprocess.Popen("{}".format(os.path.join(root,file)), stdout=devnull, stderr=devnull)
			except Exception as err:
				totalblocked += 1
				print("{} blocked. Proactive detection at {} %".format(file,(totalblocked*100)/totalrun))
			else:
				filesmissed.append(file)
				print("{} missed. Proactive detection at {} %".format(file,(totalblocked*100)/totalrun))
			sleep(5)
		except:
			pass

print("\nFinal proactive detection at {} %".format((totalblocked*100)/totalrun))	
if len(filesmissed) == 0:
		print("No files missed")
else:
	print("{} files missed: ".format(len(filesmissed)))
	for file in filesmissed:
		print("{}".format(file))
input()