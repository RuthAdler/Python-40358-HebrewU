# -*- coding: cp1255 -*-
import arcpy
arcpy.env.workspace = "C:/Users/���/Desktop/������/����� 7/arcpy/demoData.mdb"
arcpy.CreateThiessenPolygons_analysis("routes_centroids_CAL", "Thiessen", "ALL")
