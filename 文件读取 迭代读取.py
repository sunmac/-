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
#fn=tkinter.filedialog.askopenfilename(title='ѡ��һ���ļ�', filetypes=[('�����ļ�','.*'),('�ı��ļ�','.txt')])
#print(fn)
fd=r'D:\SHP2016��һ��'
for i in os.listdir(fd):
    #r.append(i)
    print i
    print os.path.isfile(fd+'\\'+i)
    if not os.path.isfile(fd+'\\'+i):
        diedai(fd+'\\'+i)



        

        
