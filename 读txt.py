# -*- coding: cp936 -*- 
import arcpy


fc="E:/1/第6批网格20160628.shp"

m=0
n=0
f=open(r'E:\old computer\2016\一体化\8月\下载edb_不带两层\123.txt')
while True:
    name=f.readline()
    name=name[0:-1]
    #print name
    if not name:break
    cursor1=arcpy.da.UpdateCursor(fc,["Text","生产管理","面积"])
    #with arcpy.da.SearchCursor(fc,["text"])as cursor:
    for row in cursor1:
        if name==row[0]:
            row[1]="下载0810"
            m=m+row[2]
            n=n+1
            print row[0]
            cursor1.updateRow(row)

del row
del cursor1
print m,n


            
                
