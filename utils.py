import os
import glob

path_train_xml = r'dataset\train_xml'
path_train = r'dataset\train'
path_test = r'dataset\test'


def list_file_name(path: str):
    file_name = []
    p = os.listdir(path)

    for i in range(len(p)):
        file_name.append(p[i])
    return file_name


def list_path(pathtrain_xml, pathtrain, pathtest):
    list_xml = glob.glob(pathtrain_xml)
    list_train = glob.glob(pathtrain)
    list_test = glob.glob(pathtest)
    return (list_xml, list_train, list_test)
def xml_parser(xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    mytree=ET.parse(xml_file)
    myroot=mytree.getroot()

    DL_DOCUMENT=root.find('{http://lamp.cfar.umd.edu/GEDI}DL_DOCUMENT')
    DL_PAGE=DL_DOCUMENT.find('{http://lamp.cfar.umd.edu/GEDI}DL_PAGE')

    list_data=[]

    for DL_ZONE in DL_PAGE:
        dic=DL_ZONE.attrib
        list_data.append(dic)

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


        else:
            pass
    signatured=[]
    if len(bounding_box)!=0:
        signatured.append(1)
    else:
        signatured.append(0)

    return( bounding_box , signatured)
