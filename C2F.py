#defined a new punction F= (Cx9)/5 +32
def c2f (r):
    return (r*9)/5+32 
#

a=input ("please input a hole number")
b=input ("please input one more hole number")
print "c --> f"
for x in range(a,b+1):
    if a<b:
        print x,"-->", c2f(x)
            
             
  
