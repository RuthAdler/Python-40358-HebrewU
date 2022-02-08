# -*- coding: cp1255 -*-
import arcpy
arcpy.env.workspace = "C:/Users/רות/Desktop/פייתון/שיעור 7/arcpy/demoData.mdb"
arcpy.Buffer_analysis("routes_COL", "buffer1km", "1 Miles", "FULL", "FLAT")
