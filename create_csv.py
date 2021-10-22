import pandas as pd

from utils import list_path, xml_parser, list_file_name

path_train_xml = r'dataset\train_xml'
path_train = r'dataset\train'
path_test = r'dataset\test'

pathtrain_xml=r'dataset\train_xml\*.xml'
pathtrain=r'dataset\train\*.tif'
pathtest=r'dataset\test\*.tif'

list_xml,list_train,list_test=list_path(pathtrain_xml,pathtrain,pathtest)


bbx=[]
ss=[]
Id=[]
d={}
for i in range(len(list_xml)):


    bounding_box , signatured=xml_parser(list_xml[i])
    name_file=list_file_name(path_train_xml)[i][:-4]
    Id.append(name_file)
    bbx.append(bounding_box)
    ss.append(signatured[0])
    d[name_file]=signatured[0]

df=pd.DataFrame(list(d.items()),columns=['Id','Expected'])
df.to_csv(r'dataset\train_class.csv', index=False)
