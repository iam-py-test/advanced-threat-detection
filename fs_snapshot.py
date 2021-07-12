import os
from hashlib import sha256
snap1 = {}
snap2 = {}
for root, files, dirs in os.walk("/"):
  for file in files:
    snap1[os.path.join(root,file)] = sha256(open(os.path.join(root,file),"rb")).hexdigest()
print(snap1)

cont = input("Press enter to continue: ")
for root, files, dirs in os.walk("/"):
  for file in files:
    filename = os.path.join(root,file)
    try:
      oldsha = snap1[filename]
    except:
      print("File created: {}".format(filename))
    else:
      if sha256(open(filename,"rb")).hexdigest() == oldsha:
        continue
      else:
        print("File {} changed: {} --> {}".format(filename,oldsha,sha256(open(filename,"rb")).hexdigest()))
    
