# -*- coding: cp936 -*- 
import os
import arcpy
from arcpy import env

r=[]
ploygen=[r'HFCA','HYDA','RESA','BUIA','RDA','RRFCA','RDFCA','PPFCA','TERA']
ploygen1=[r'HFCA','HYDA','RESA','BUIA','RDA','RRFCA','RDFCA','PPFCA','TERA']
line=['HYDFCL','RESL','RRL','RDSL','RDL','RRFCL','RDFCL','PPFCL','TERL','CONL','VEGL']
env.workspace = "d:/data"
out=r"D:\123\123.gdb\shiyan\\"
count=0
for i in line:
    out1=out[:len(out)-1]+i
    print out1
    arcpy.AddRuleToTopology_management(r"D:\123\123.gdb\shiyan\tuopu", "Must Not Overlap (Line)",out1,"","","",)
for i in ploygen:
    for j in ploygen1[count:]:
        if i!=j:
            out1=out[:len(out)-1]+i
            out2=out[:len(out)-1]+j
            print out1
            print out2
            arcpy.AddRuleToTopology_management(r"D:\123\123.gdb\shiyan\tuopu","Must Not Overlap With (Area-Area)",out1,"",out2,"",)
    count=count+1
for i in ploygen:
    out1=out[:len(out)-1]+i
    print out1
    arcpy.AddRuleToTopology_management(r"D:\123\123.gdb\shiyan\tuopu", "Must Not Overlap (Area)",out1,"","","",)
#for i in line:
 #   in_feature1 = fd+i+".shp"
  #  print in_feature1
   # for j in line:
    #    in_feature2=fd+j+'.shp'
     #   if i!=j:
      #      out="D:/123.gdb/exper/"+i+j
       #     print out
        #    arcpy.CreateTopology_management ("D:/123.gdb/exper/", i+j,)
         #   arcpy.AddRuleToTopology_management(out, "Must Not Overlap (Line)",i,"","","",)


# Set workspace

#arcpy.CheckGeometry_management ()


        
