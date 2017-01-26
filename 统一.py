# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-
import arcpy
import arcgisscripting
import os
gp=arcgisscripting.create(10)
#输入edb文件夹
fd=gp.GetParameterAsText(0)
#fd = "E:\old computer"
#fd.decode
#输入shp路径
fc=gp.GetParameterAsText(1)
#输入名称
shuru=gp.GetParameterAsText(2)
r=[]
m=0
n=0
#print fc
#print fd
#fd="11111"
gp.SetProgressorLabel(fc)
#fd=r'E:\old computer\2016\一体化\8月\改高程8.1'
#fc=r'E:\1\实验\第6批网格20160628.shp'
#shuru=u'改高程'
#gp.SetProgressorLabel(os.listdir(fd))
#fd.encode('utf-8')
for i in os.listdir(fd):
    i=i.replace(r'_GIS2000_20160512_Download.log','')
    i=i.replace(u'_GIS2000_20160512_更新备份数据.edb','')
    i=i.replace(r'_GIS2000_20160512.edb','')
    i=i.replace(r'.edb','')
    r.append(i)


r2=sorted(set(r),key=r.index)
for i in r2:
    n=1
    print i
    
for name in r2:
    cursor1=arcpy.da.UpdateCursor(fc,["Text","生产管理","面积"])
    #with arcpy.da.SearchCursor(fc,["text"])as cursor:
    for row in cursor1:
        if name==row[0]:
            row[1]=shuru
            m=m+row[2]
            n=n+1
            print row[0]
            cursor1.updateRow(row)

del row
del cursor1

print m,n
