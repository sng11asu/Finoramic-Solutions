import subprocess
import json
import sys
sucess=[]
fail=[]
a = []
def install(package):
	#call the subprocess.run() passing "pip install package" as argumet
    a=subprocess.run(["pip","install",package])
    # store successfully installed package to the success list
    if a.returncode == 0:
        sucess.append(package)
    # store failed packages in fail list
    else:
        fail.append(package)
 # open json file in read mode
f = open("xyz.json", "r")
s = f.read()
#load as string in d
d = json.loads(s)
#for each value in d call install()
for i in d:
    install(d[i])
#print list of successfully installed and failed processes
print("Packages Succeded:-",end=" ")
print(sucess)
print("Packages Failed:-",end=" ")
print(fail)
