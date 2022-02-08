f1=open("c:/Hallelujah.txt","r")
f2=open("c:/Frank's Tavern.txt","r")

read1=f1.read()
read2=f2.read()

words1=read1.split()
words2=read2.split()

set1=set(words1)
set2=set(words2)

print set1
print set2

set3=set1|set2
print set3

set1spatial=set1-set2
print set1spatial

set2spatial=set2-set1
print set2spatial

f1.close()
f2.close()
