f=open("C:/text.txt","r")
x=f.readline()
print x.center(60)
f.close ()

f=open("C:/text.txt","r")
for line in f:
    print line
f.close()

f=open("C:/text.txt","r")
list1=f.readlines()
y=list1[-1]
print y.title()
f.close ()

f2=open("C:/new.txt","w")
for i in list1:
    f2.write(i)
f2.close()

