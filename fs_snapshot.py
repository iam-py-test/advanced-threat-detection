import os
import hashlib
snap1 = {}
snap2 = {}
for root, dirs, files in os.walk("/"):
  for file in files:
    try:
      snap1[os.path.join(root,file)] = hashlib.sha256(open(os.path.join(root,file),"r").encode()).hexdigest()
    except Exception as err:
      print(err)
print(snap1)

cont = input("Press enter to continue: ")
for root, dirs, files in os.walk("/"):
  for file in files:
    filename = os.path.join(root,file)
    try:
      oldsha = snap1[filename]
    except:
      print("File created: {}".format(filename))
    else:
      if hashlib.sha256(open(filename,"r").encode()).hexdigest() == oldsha:
        continue
      else:
        print("File {} changed: {} --> {}".format(filename,oldsha,hashlib.sha256(open(filename,"rb")).hexdigest()))
    
