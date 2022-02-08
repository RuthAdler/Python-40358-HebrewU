#2 steps:defined a+b+c so while can ran,then-mishtane between b-c that mithalek
#in a.
a=3
b=2
c=1
while a>b>c or b>a>c or c>a>b or a>c>b or b>c>a:
    a=input("pleas enter the smallest number")
    b=input("pleas enter the middle number")
    c=input("pleas enter the bigger number")
    if a>b>c or b>a>c or c>a>b or a>c>b or b>c>a:
        print "your numbers wasn't good,try again"
    else:
        for i in range(b,c):
            if i%a==0:
                print i
