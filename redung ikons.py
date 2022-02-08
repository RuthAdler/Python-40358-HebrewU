#1
f=open("C:/text.txt", "r")
#2
for line in f:
    print line
f.close()

#3
f=open("C:/text.txt", "r")
c=0
listy=f.readlines()
print len(listy)

#4
f=open("C:/text.txt", "r")
print listy[4]

