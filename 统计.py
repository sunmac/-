# -*- coding: cp936 -*- 
import arcpy  
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
fc="E:/1/��6������20160628.shp"
mianji1=0
mianji2=0
m=0
m1=0
m2=0
zongmianji=0
cursor1=arcpy.da.UpdateCursor(fc,["Text","��������","���"])
for row in cursor1:    
    zongmianji=zongmianji+row[2]
    if row[1]==u'���������' or  row[1]==u'���' or row[1]==u'���0727'or row[1]==u'���0808':
        m=m+1
        mianji1=mianji1+row[2]
    if row[1]==u'����'or row[1]==u'����0729'or row[1]==u'����0810':
        m1=m1+1
        mianji2=mianji2+row[2]
    if row[1]==u'����0810':
        m2=m2+1
print u'���δ���ظ���',m,u'���δ�������',mianji1,u'ռ��',mianji1/zongmianji
print u'�����ظ���',m1,u'�������',mianji2,u'ռ��',mianji2/zongmianji
a=mianji2/zongmianji+mianji1/zongmianji
print u'�����',zongmianji,u'����������',mianji1+mianji2,u'ռ��',a
print m2
del row
del cursor1

