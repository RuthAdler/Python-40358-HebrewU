#targil kita 1-1
number=9
while number<100:
    print number
    number=number*2

#targil 1-2
a=0
b=1
while a<1000:
    print a
    c=a
    a=b
    b=c+b
    
    
#targil 1-3

number=1
while number<=20:
    
    a=input("pleaes enter a number")
    if a%3==0 and a%5==0 and a%7==0:
         print "BimBamBum"
    elif a%3==0 and a%5!=0 and a%7!=0: 
        print "Bim"
    elif a%5==0 and a%3!=0 and a%7!=0:
        print "Bam"
    elif a%7==0 and a%3!=0 and a%5!=0:
        print "Bum"
    elif a%3==0 and a%5==0 and a%7!=0:
        print "BimBam"
    elif a%5==0 and a%7==0 and a%3!=0:
        print "BamBum"
    elif a%3==0 and a%7==0 and a%5!=0:
        print "BimBum"

    number+=1
    

