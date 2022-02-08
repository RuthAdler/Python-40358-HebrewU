def concord(a):
    b=a.split()
    b.sort()
    L=[]
    for i in b:
        if i not in L:
            L.append(i)
    for x in L:
        v=b.count(x)
        print x,":",v
        

concord ("Why do the sun go on shining? Why do these eyes of mine cry?")      
        
