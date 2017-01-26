# -*- coding: cp936 -*- 
import arcpy  
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
fc="E:/1/第6批网格20160628.shp"
mianji1=0
mianji2=0
m=0
m1=0
m2=0
zongmianji=0
cursor1=arcpy.da.UpdateCursor(fc,["Text","生产管理","面积"])
for row in cursor1:    
    zongmianji=zongmianji+row[2]
    if row[1]==u'入库有问题' or  row[1]==u'入库' or row[1]==u'入库0727'or row[1]==u'入库0808':
        m=m+1
        mianji1=mianji1+row[2]
    if row[1]==u'下载'or row[1]==u'下载0729'or row[1]==u'下载0810':
        m1=m1+1
        mianji2=mianji2+row[2]
    if row[1]==u'下载0810':
        m2=m2+1
print u'入库未下载个数',m,u'入库未下载面积',mianji1,u'占比',mianji1/zongmianji
print u'已下载个数',m1,u'下载面积',mianji2,u'占比',mianji2/zongmianji
a=mianji2/zongmianji+mianji1/zongmianji
print u'总面积',zongmianji,u'入库数据面积',mianji1+mianji2,u'占比',a
print m2
del row
del cursor1

