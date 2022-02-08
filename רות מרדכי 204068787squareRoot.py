#add your numers and caculat x1+x2.you must put() in eny places needed.
a=input("please insert a")
b=input("please insert b")
c=input("please insert c")
#x1=(-b+sqrt(b2-4*a*c))/(2*a)
#x2=(-b+sqrt(b2-4*a*c))/(2*a)
import math
calc_sqrt=math.sqrt((b**2)-(4*a*c))
calc_all1=(-b+(calc_sqrt))/(2*a)

calc_all2=(-b-(calc_sqrt))/(2*a)

print "The answer is: x1=",calc_all1,"and x2=",calc_all2
