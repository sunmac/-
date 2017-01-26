# -*- coding: cp936 -*-
import arcpy
from arcpy import env
import os
def diedai(path):
    for i in os.listdir(path):
        print i
        print os.path.isfile(path+'\\'+i)
        if not os.path.isfile(path+'\\'+i):
            diedai(path+'\\'+i)
r=[]
#import tkinter.filedialog
#fn=tkinter.filedialog.askopenfilename(title='选择一个文件', filetypes=[('所有文件','.*'),('文本文件','.txt')])
#print(fn)
fd=r'D:\SHP2016第一轮'
for i in os.listdir(fd):
    #r.append(i)
    print i
    print os.path.isfile(fd+'\\'+i)
    if not os.path.isfile(fd+'\\'+i):
        diedai(fd+'\\'+i)



        

        
