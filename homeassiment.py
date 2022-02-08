#targil8-1
f=open("C:/text.txt", "r")
lineList=f.readline()
lineList.center(150)+"\n"

f=open("C:/text.txt", "r")
last=f.readlines()
last.title()
f.close()
#3#4
fnew=open("C:/text.txt", "w")
for line in lineList:
    fnew.write(line)
fnew.close()
