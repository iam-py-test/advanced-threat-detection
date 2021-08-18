import os
import subprocess
from time import sleep

dir = input("Enter the dir to use:")
totalrun = 0
totalblocked = 0
filesmissed = []
totallog = 'Begin malrun log. Using dir \"{}\"'.format(dir)

for root,dirs,files in os.walk(dir):
	for file in files:
		try:
			print("Running {}".format(file))
			totallog += "\nRan {}".format(file)
			totalrun += 1
			try:
				devnull = open(os.devnull, 'wb')
				subprocess.Popen("{}".format(os.path.join(root,file)), stdout=devnull, stderr=devnull)
			except Exception as err:
				totalblocked += 1
				totallog += "\n{} blocked. Proactive detection at {} %".format(file,(totalblocked*100)/totalrun)
				print("{} blocked. Proactive detection at {} %".format(file,(totalblocked*100)/totalrun))
			else:
				filesmissed.append(file)
				totallog += "\n{} missed. Proactive detection at {} %".format(file,(totalblocked*100)/totalrun)
				print("{} missed. Proactive detection at {} %".format(file,(totalblocked*100)/totalrun))
			with open("malrun_log.txt","w") as f:
				f.write(totallog)
				f.close()
			sleep(5)
		except:
			pass

print("\n{} files run. Final proactive detection at {} %".format(totalrun,(totalblocked*100)/totalrun))	
totallog += "\n------------------------------------------------------------\n{} files run. Final proactive detection at {} %".format(totalrun,(totalblocked*100)/totalrun)
with open("malrun_log.txt","w") as f:
	f.write(totallog)
	f.close()
totallog += "\n\n{} files missed: ".format(len(filesmissed))
if len(filesmissed) == 0:
		print("No files missed")
else:
	print("{} files missed: ".format(len(filesmissed)))
	for file in filesmissed:
		print("{}".format(file))
		totallog += "\n{}".format(file)
with open("malrun_log.txt","w") as f:
	f.write(totallog)
	f.close()
input()
