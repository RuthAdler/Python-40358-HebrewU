# -*- coding: cp1255 -*-
import arcpy
arcpy.env.workspace = "C:/Users/רות/Desktop/פייתון/שיעור 7/arcpy/demoData.mdb"
for i in range (0,6):
    import random
    i=random.randint(1,30)
    if i==i:
        i=random.randint(1,30)
    arcpy.Buffer_analysis("routes_COL", "buffer"+str(i), str(i)+" Kilometers")
    print (i)

