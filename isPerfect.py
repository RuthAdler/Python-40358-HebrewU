

def isperfect(a):
    m=0
    for x in range (1,a):
        if a%x==0:
            m=m+x
        else:
            m=m+0
            
        
    if a==m:
       return True
    else:
        return False

num=input ("plaese input a")
Num= input ("please input b that a<b")

for i in range (num,Num):
    if isperfect(i)==True:
        print i        





