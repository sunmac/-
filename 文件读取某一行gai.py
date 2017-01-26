# -*- coding: cp936 -*- 
import os
r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
#import tkinter.filedialog
#fn=tkinter.filedialog.askopenfilename(title='选择一个文件', filetypes=[('所有文件','.*'),('文本文件','.txt')])
#print(fn)
fd=r'D:\\新建文件夹 (2)'
abc=r'\\'
for i in os.listdir(fd):
    
    abc=fd+ r'\\' +i
    
   # print abc
    fa=open(abc,'r')
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
  #  print ab
    ab=ab[-2:]
    r3.append(ab)
    ab=fa.readline()
    ab=fa.readline()
   # print ab
    ab=ab[-7:]
    r5.append(ab)
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    print ab
    ab=ab[-2:]
    r4.append(ab)
    ab=fa.readline()

    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=fa.readline()
    ab=ab[-7:]
   # print ab[-7:]
    r2.append(ab)
    ab=fa.readline()
   # print ab
    
    r1.append(i)

j=0
fd=fd+'\\原图测图日期.txt'
f=open(fd,'w')
for i in r1:
    i=i.replace('.mat','')
    r2[j]=r2[j].replace('\n','')
    r3[j]=r3[j].replace('\n','')
    r4[j]=r4[j].replace('\n','')
    r5[j]=r5[j].replace('\n','')
    i=i+','+r3[j]+','+r2[j]+','+r5[j]+','+r4[j]+'\n'
    f.writelines(i)
    j=j+1
print 
f.close()

