# -*- coding: cp936 -*- 
import os
r=[]
#import tkinter.filedialog
#fn=tkinter.filedialog.askopenfilename(title='ѡ��һ���ļ�', filetypes=[('�����ļ�','.*'),('�ı��ļ�','.txt')])
#print(fn)
fd=r'D:\edb����'
for i in os.listdir(fd):
    i=i.replace('_GIS2000_20160512_Download.log','')
    i=i.replace('_GIS2000_20160512_���±�������.edb','')
    i=i.replace('_GIS2000_20160512.edb','')
    i=i.replace('.edb','')
    r.append(i)


r2=sorted(set(r),key=r.index)

for i in r2:
    print i
fd=fd+'\123.txt'
f=open(fd,'w')
for i in r2:   
    i=i+'\n'
    f.writelines(i)
print 
f.close()


        

        
