#the user input his number/targil 3

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
