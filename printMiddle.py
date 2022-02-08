#the program will choose the middle number
a=input ("please enter a number")
b=input ("please enter a number")
c=input ("please enter a number")
if a<b<c:
    print b
elif c<b<a:
    print b
elif c<a<b:
    print a
elif b<a<c:
    print a
elif b<c<a:
    print c
elif a<c<b:
    print c
