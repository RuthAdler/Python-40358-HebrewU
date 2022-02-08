# learn how to get numer in a spedufic location,
text="You are my"
print len (text)
print text [1]
print text[0]
print text [2],text [3]
print text [-1]
print text [-2]
#and how to get the midlle in the machrozet. in 2 ways
machrozet="hao gu nguu ytr ytfdes vcdgjn,jjdhgaustyhfjklociy3yucrbyui"

mid=(len(machrozet)-1)/2

print machrozet[mid]
midlle =len(machrozet)/2
print machrozet[midlle]

#a few simbls from the machrozet
machrozettwo="kwjgfusycbyc"
print machrozettwo[3:7]
print machrozettwo[4:len(machrozettwo)]
print machrozettwo[3:]
print machrozettwo[:4]
print machrozettwo[:]
print machrozettwo[-3:]
print machrozettwo[-3:]+ machrozettwo[-8:-5]
#targil cita 2
#1
hamesh="how much i love you"
print hamesh[0:3]
print hamesh[4:9]
print hamesh[9]
print hamesh[-8:-4]
print hamesh[-3:len(hamesh)]
#2
print hamesh[-3:]+ hamesh[-8:-4]+hamesh[9]+hamesh[4:9]+hamesh[0:3]
#3
textt=raw_input("please input your machrozet")
print "the last 5 numbers are", textt[-5:]


#targil 4
#1
mylist=[14,"ruth",505,"yehudit"]
print mylist[0:3]
print mylist[2]
print mylist[3]
longlist=["ghdgf",434,878,45,"gh","yft"]
print mylist[0:]+longlist[0:]
#2
shemone=[67,67,98,765,"dgfgh","gfh","fhg","fgbfh"]
#3
import random
print random.randint(0,500)
randomindex=random.randint(0,7)
print shemone [randomindex]
