# -*- coding: cp936 -*-
import arcpy
from arcpy import env
import os
clip_features = r"E:\123.shp"
fd=r'D:\SHP2016第一轮'
out=r'D:\新建文件夹'
def diedai(path):
    r=[]
    os.makedirs(out+path.replace(fd,''))
    for i in os.listdir(path):
        if not os.path.isfile(path+'\\'+i):
            r.append(diedai(path+'\\'+i))
        else:
            i= os.path.splitext(i)[0]
            if 'shp'  in i:

                i= path+'\\'+i
                j=i.replace(fd,'')
                j=out+j
                print j
                arcpy.Clip_analysis(i, clip_features, j, '')
    return r 
r=[]
env.workspace = "d:/data"
r=[]
for i in os.listdir(fd):
    if not os.path.isfile(fd+'\\'+i):
        r.append(diedai(fd+'\\'+i))
    else:
        r.append(path+'\\'+i)
        i= path+'\\'+i
        j=i.replace('D:\SHP2016第一轮','')
        j=out+j
        print j

        

        
