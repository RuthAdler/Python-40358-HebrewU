#random song from list
peopleNames=['Iosi','Ety','moty','michal','hila','ruth']
verbs=['sees','plays','sings','cooks','bakes','drink']
Adjectives=['tall','small','red','big','nice','huge']
Objects=['stone','chair','dog','friends','apple','computer']

import random
songrandom=random.randint(0,6)

print  peopleNames[songrandom],verbs[songrandom],Adjectives[songrandom],Objects[songrandom]
