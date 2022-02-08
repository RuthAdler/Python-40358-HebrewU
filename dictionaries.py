rID=open("c:/ID.txt","r")
rNAME=open("c:/Name.txt","r")
rtelephone=open("c:/telephone.txt","r")
ID= rID.readlines()
NAME= rNAME.readlines()
telephone=rtelephone.readlines()

for i in range(len(ID)):
    ID[i]=ID[i].strip("\n")
for i in range(len(NAME)):
    NAME[i]=NAME[i].strip("\n")
for i in range(len(telephone)):
    telephone[i]=telephone[i].strip("\n")

Dict={}
for i in range(len(ID)):
    Dict[ID[i]]=[NAME[i],telephone[i]]
print "Dict:",Dict
print " "

tDict={}
for i in range(len(ID)):
    tDict[NAME[i],telephone[i]]=[ID[i]]
print tDict

    
