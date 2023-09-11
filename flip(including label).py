import numpy as np
import cv2
import xml.etree.ElementTree as ET
from PIL import Image
 
name_classes = ['vannamei']  # 类别名，可以更改为对应的voc类别名称即可
 
def flip_horizontal(jpg_file,new_jpg):
    img = Image.open(jpg_file)
    # png =Image.open(png_file)
    # out = im.transpose(Image.ROTATE_180)
    out_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    # out_png = png.transpose(Image.FLIP_LEFT_RIGHT)
 
    out_img.save(new_jpg)
    # out_png.save(new_png)
    return img.width,img.height

def flip_vertical(jpg_file,new_jpg):
    img = Image.open(jpg_file)
    # png =Image.open(png_file)
    # out = im.transpose(Image.ROTATE_180)
    out_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    # out_png = png.transpose(Image.FLIP_LEFT_RIGHT)
 
    out_img.save(new_jpg)
    # out_png.save(new_png)
    return img.width,img.height  
def flip_90_xml(xml_file,new_xml,image_width,image_height):
    tree = ET.parse(xml_file)
    objs = tree.findall('object')
    for ix, obj in enumerate(objs):
        name = obj.find('name').text
        if name in name_classes:           # 因为本数据集只针对某一个更改的，你要改的有很多，此处要改为 if name in name_classes :
            print(xml_file)
            obj_new = obj.find('bndbox')
            xmin = str( image_width - int(obj_new.find('xmax').text))     # 因为进行水平翻转，这只改变x坐标值，y坐标值不变
            xmax = str( image_width - int(obj_new.find('xmin').text))     # 此处256是图片的宽和高，水平翻转，最大值变最小值，最小值变最大值
            obj_new.find('xmin').text = xmin
            obj_new.find('xmax').text = xmax
            tree.write(new_xml)

def flip_180_xml(xml_file,new_xml,image_width,image_height):
    tree = ET.parse(xml_file)
    objs = tree.findall('object')
    for ix, obj in enumerate(objs):
        name = obj.find('name').text
        if name in name_classes:           # 因为本数据集只针对某一个更改的，你要改的有很多，此处要改为 if name in name_classes :
            print(xml_file)
            obj_new = obj.find('bndbox')
            ymin = str( image_height - int(obj_new.find('ymax').text))     # 因为进行水平翻转，这只改变x坐标值，y坐标值不变
            ymax = str( image_height - int(obj_new.find('ymin').text))     # 此处256是图片的宽和高，水平翻转，最大值变最小值，最小值变最大值
            obj_new.find('ymin').text = ymin
            obj_new.find('ymax').text = ymax
            tree.write(new_xml) 
 
if __name__ == '__main__':
    # 原始的图片，xml，png数据集的路径

    xml_file=r'vannamei16867.xml'
    jpg_file=r'vannamei16867.jpg'
    
    
    # 水平翻转后保存的路径
    new_jpg=r'flip_v_vannamei16867.jpg'
    new_xml = r'flip_v_vannamei16867.xml'

    
    
    wid,hei = flip_horizontal(jpg_file, new_jpg)
    flip_90_xml(xml_file, new_xml,wid,hei)
   
    image =Image.open(new_jpg)
    tree = ET.parse(new_xml)
    root = tree.getroot()
    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text
 
        cls = obj.find('name').text
        if cls not in name_classes or int(difficult) == 1:
            continue
        cls_id = name_classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        print(b)
 
    # image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    # cv_img = cv2.rectangle(image, (int(float(b[0])),
    #                                int(float(b[1]))),
    #                        (int(float(b[2])),
    #                         int(float(b[3]))), (255, 0, 0), 2)
 
    # image = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
    # image.show()
    
    # new_jpg1=r'flip_v_vannamei16867.jpg'
    # new_xml1 = r'flip_v_vannamei16867.xml'
    # wid,hei = flip_horizontal(jpg_file, new_jpg1)
    # flip_180_xml(xml_file, new_xml1,wid,hei)