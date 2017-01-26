# -*- coding: cp936 -*- 
import os
import arcpy
from arcpy import env
r=[]
#import tkinter.filedialog
#fn=tkinter.filedialog.askopenfilename(title='选择一个文件', filetypes=[('所有文件','.*'),('文本文件','.txt')])
#print(fn)
fd=r'D:\GIS2000_20160901_shp'#输入文件夹
out=r'D:\clip\4\\'#输出文件夹
for i in os.listdir(fd):
    if i.find('shp')>0 and i.find('xml')<0 :
        r.append(i)
        print i
fd=fd+'\\'
env.workspace = "d:/data"
for i in r:
    in_features = fd+i
    clip_features = r"E:\1\4.shp"#cilp文件
    out_feature_class = out+i
    xy_tolerance = ""
    print out_feature_class
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)




        
