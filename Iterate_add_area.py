import arcpy
env.workspace = "E:/Hayden Working/test"
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    arcpy.AddField_management(fc, "Area_ha", "DOUBLE")
    arcpy.CalculateField_management(fc, "Area_ha", "!shape.area@meters!", "PYTHON");