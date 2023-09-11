import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir , getcwd
from os.path import join
import glob
origan_file='G:\\image_datasets\\jh1\\label\\'
save_file='G:\\image_datasets\\jh1\\label_txt\\'
classes = ["person"]
 
def convert(size, box):
 
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(image_name):
    in_file = open(origan_file+image_name+'.xml','r',encoding='UTF-8') 
    out_file = open(save_file+image_name+'.txt', 'w',encoding='UTF-8') 
    f = open(origan_file+image_name+'.xml',encoding='UTF-8')
    xml_text = f.read()
    root = ET.fromstring(xml_text)
    f.close()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
 
 
 
 
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
wd = getcwd()
 
if __name__ == '__main__':
 
    for image_path in glob.glob(origan_file+"*.xml"): 
        image_name= image_path.split('\\')[4]  #number may change
        """ print(os.path.splitext(image_name)[0]) """
        convert_annotation(os.path.splitext(image_name)[0])
