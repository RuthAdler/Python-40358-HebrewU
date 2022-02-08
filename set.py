seta={1,9,9,2,0,3,0,6}
seta.add(('world','hila'))
print seta
seta.discard(3)
            
for i in seta:
    print i

listy=[67,"yu",890,890,"yu"]
setb=set(listy)
print setb

#targil
list1=range(1,101)
list2=range (50,101)
               
set1=set(list1)
set2=set(list2)
set3=set1 | set2
print set3

set4=set1-set2
print set4

set5=set1.intersection(set2)
print set5
