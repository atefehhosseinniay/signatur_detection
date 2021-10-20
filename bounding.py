import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import matplotlib
from matplotlib import patches

image=Image.open(r'C:\Users\atefe\Desktop\b_d\train\0d178d095434170eac2cb58cc244bb8c_2.tif')
plt.imshow(image)
#plt.show()

with open(r'C:\Users\atefe\Desktop\b_d\train_xml\0d178d095434170eac2cb58cc244bb8c_2.xml') as annotated_file:
    print(''.join(annotated_file.readlines()))

tree = ET.parse(r'C:\Users\atefe\Desktop\b_d\train_xml\0d178d095434170eac2cb58cc244bb8c_2.xml')
root = tree.getroot()

DL_DOCUMENT=root.find('{http://lamp.cfar.umd.edu/GEDI}DL_DOCUMENT')
DL_PAGE=DL_DOCUMENT.find('{http://lamp.cfar.umd.edu/GEDI}DL_PAGE')
list_data=[]
for DL_ZONE in DL_PAGE:
    dic=DL_ZONE.attrib
    list_data.append(dic)
#print(list_data)
bounding_box=[]
for i in range(len(list_data)):
    if list_data[i]['gedi_type']=='DLSignature':
        ymin=int(list_data[i]['row'])
        ymax=int(list_data[i]['row'])+int(list_data[i]['height'])
        height=int(list_data[i]['height'])
        xmin=int(list_data[i]['col'])
        xmax=int(list_data[i]['col'])+int(list_data[i]['width'])
        width=int(list_data[i]['width'])
        bounding_box.append([xmin,ymin,xmax,ymax])
        #bounding_box.append([xmin, ymax, width, height])
        print(bounding_box)
    else:
        pass
image_1=cv.imread(r'C:\Users\atefe\Desktop\b_d\train\0d178d095434170eac2cb58cc244bb8c_2.tif')
#im_annotated=image_1.copy()
#image_bbx=ImageDraw.Draw(im_annotated)
for bbox in bounding_box:
    im= cv.rectangle(image_1,(bbox[0],bbox[3]), (bbox[2],bbox[1]), (0, 255, 0), 2)
    plt.imshow(im)
plt.show()



#print(root.tag)
#for child in root:
#print(child.tag, child.attrib)


#for DL_ZONE in root.iter('DL_ZONE'):print(DL_ZONE.attrib)


