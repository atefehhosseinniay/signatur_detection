import xml.etree.ElementTree as ET

# create list of all xml files
import os
file_path=r'C:\Users\atefe\Desktop\b_d\train_xml'
file_name=[]
p=os.listdir(file_path)
for i in range(len(p)):
    file_name.append(p[i])

#print(file_name)
#print(len(file_name))
# list of all string of files
doc=[]
for file in file_name:
    file_p=os.path.join(file_path,file)
    with open (file_p,'r') as f:
        data=f.read()
        doc.append(data)
print(len(doc))
# check if document is signed or not
signed_file=0
unsigned_file=0
import re
dic={}
signed=[]
unsigned=[]
for i in range(len(doc)):
    if re.search(r'DLSignature', doc[i])!=None:
        signed_file+=1
        key=file_name[i][:-4]
        signed.append(key)
        dic.update({f'{key}':1})
    if re.search(r'DLSignature', doc[i]) == None:
        unsigned_file+=1
        key1 = file_name[i][:-4]
        unsigned.append(key1)
        dic.update({f'{key1}': 0})

#print(signed,unsigned)
#create data Frame
import pandas as pd
item=dic.items()
data_list=list(item)
df=pd.DataFrame(data_list,columns=['Id','Expected'])
print(df)

print(signed)
print(len(signed))
print(unsigned)
print(len(unsigned))



#print(dic)
df.to_csv(r'C:\Users\atefe\Desktop\b_d\signature.csv')


# create 2 class image
file_path1=r'C:\Users\atefe\Desktop\b_d\train'
signed_train=[]
unsigned_train=[]
a=os.listdir(file_path1)
for i in range(len(a)):
    if a[i][:-4] in signed:
        signed_train.append(a[i])
    if a[i][:-4] in unsigned:
        unsigned_train.append(a[i])

print(signed_train)
print(unsigned_train)

'''
import shutil
path_train=r'C:\Users\atefe\Desktop\b_d\train'
for file in signed_train:
    im=os.path.join(f'{file}',path_train)
    shutil.copy(im,r'C:\Users\atefe\Desktop\b_d\train2')
    '''






