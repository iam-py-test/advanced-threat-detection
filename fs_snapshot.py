import os
import hashlib
snap1 = {}
snap2 = {}
def arg(p):
  try:
    import sys
    return sys.argv[p]
  except:
    return None
  
dirtowalk = "/"
if arg(1) == "-d":
  dirtowalk = arg(2)
for root, dirs, files in os.walk(dirtowalk):
  for file in files:
    try:
      snap1[os.path.join(root,file)] = hashlib.sha256(open(os.path.join(root,file),"rb").read()).hexdigest()
    except Exception as err:
      pass
#print(snap1)

cont = input("Press enter to continue: ")
for root, dirs, files in os.walk(dirtowalk):
  for file in files:
    filename = os.path.join(root,file)
    snap2[filename] = hashlib.sha256(open(filename,"rb").read()).hexdigest()
    try:
      oldsha = snap1[filename]
    except:
      print("File created: {}".format(filename))
    else:
      if hashlib.sha256(open(filename,"rb").read()).hexdigest() == oldsha:
        continue
      else:
        print("File {} changed: {} --> {}".format(filename,oldsha,hashlib.sha256(open(filename,"rb").read()).hexdigest()))
    
for file in snap1:
  try:
    newf = snap2[file] 
  except:
    print("{} has been deleted or renamed".format(file))
  
