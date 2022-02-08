-#
number=0
while number<15: 
    peopleNames=['Iosi','Ety','moty','michal','hila','ruth']
    verbs=['sees','plays','sings','cooks','bakes','drink']
    Adjectives=['tall','small','red','big','nice','huge']
    Objects=['stone','chair','dog','friends','apple','computer']

    import random
    a=random.randint(0,len(peopleNames)-1)
    b=random.randint(0,len(verbs)-1)
    c=random.randint(0,len(Adjectives)-1)
    d=random.randint(0,len(Objects)-1)
    print peopleNames[a], verbs[b], Adjectives[c], Objects[d] 

    number=number+1
