import os
import numpy as np
import cv2
import math
import xml.etree.ElementTree as ET
from PIL import Image
 
 

def rotate_img(src, angle, scale=1):
    width = src.shape[1]      # org_wid
    height = src.shape[0]     # org_hei
    # degree to rad
    re_angle = np.deg2rad(angle)
    # new img wid and hei
    new_width = (abs(np.sin(re_angle) * height) + abs(np.cos(re_angle) * width)) * scale
    new_height = (abs(np.cos(re_angle) * height) + abs(np.sin(re_angle) * width)) * scale
 
    rotate_matrix = cv2.getRotationMatrix2D((new_width * 0.5, new_height * 0.5), angle, scale)
    rotate_move = np.dot(rotate_matrix, np.array([(new_width - width) * 0.5, (new_height - height) * 0.5, 0]))
 
    # update translation
    rotate_matrix[0, 2] += rotate_move[0]
    rotate_matrix[1, 2] += rotate_move[1]
 
    dst = cv2.warpAffine(img, rotate_matrix, (int(math.ceil(new_width)), int(math.ceil(new_height))),
                         flags=cv2.INTER_LANCZOS4)
    return dst
 
 

def rotate_xml(src, xmin, ymin, xmax, ymax, angle, scale=1):
    if angle%90==0:
        width = src.shape[1]
        height = src.shape[0]
        re_angle = np.deg2rad(angle)
        new_width = (abs(np.sin(re_angle) * height) + abs(np.cos(re_angle) * width)) * scale
        new_height = (abs(np.cos(re_angle) * height) + abs(np.sin(re_angle) * width)) * scale
        rotate_matrix = cv2.getRotationMatrix2D((new_width * 0.5, new_height * 0.5), angle, scale)
        rotate_move = np.dot(rotate_matrix, np.array([(new_width - width) * 0.5, (new_height - height) * 0.5, 0]))
        rotate_matrix[0, 2] += rotate_move[0]
        rotate_matrix[1, 2] += rotate_move[1]
        
        point1 = np.dot(rotate_matrix, np.array([(xmin + xmax) / 2, ymin, 1]))
        point2 = np.dot(rotate_matrix, np.array([xmax, (ymin + ymax) / 2, 1]))
        point3 = np.dot(rotate_matrix, np.array([(xmin + xmax) / 2, ymax, 1]))
        point4 = np.dot(rotate_matrix, np.array([xmin, (ymin + ymax) / 2, 1]))
        concat = np.vstack((point1, point2, point3, point4))  
        
        concat = concat.astype(np.int32)
        rx, ry, rw, rh = cv2.boundingRect(concat)  
        new_xmin = rx
        new_ymin = ry
        new_xmax = rx + rw
        new_ymax = ry + rh
    
        return new_xmin, new_ymin, new_xmax, new_ymax
    else:
        width = src.shape[1]
        height = src.shape[0]
        re_angle = np.deg2rad(angle)
        new_width = abs(height*np.cos(re_angle))+abs(width*np.sin(re_angle))
        new_height = abs(width*np.cos(re_angle))+abs(height*np.sin(re_angle))
        rotate_matrix = cv2.getRotationMatrix2D((new_width * 0.5, new_height * 0.5), angle, scale)
        rotate_move = np.dot(rotate_matrix, np.array([(new_width - width) * 0.5, (new_height - height) * 0.5, 0]))
        rotate_matrix[0, 2] += rotate_move[0]
        rotate_matrix[1, 2] += rotate_move[1]
        point1 = np.dot(rotate_matrix, np.array([(xmin + xmax) / 2, ymin, 1]))
        point2 = np.dot(rotate_matrix, np.array([xmax, (ymin + ymax) / 2, 1]))
        point3 = np.dot(rotate_matrix, np.array([(xmin + xmax) / 2, ymax, 1]))
        point4 = np.dot(rotate_matrix, np.array([xmin, (ymin + ymax) / 2, 1]))
        concat = np.vstack((point1, point2, point3, point4))  
        
        concat = concat.astype(np.int32)
        rx, ry, rw, rh = cv2.boundingRect(concat)  
        new_xmin = rx
        new_ymin = ry
        new_xmax = rx + rw
        new_ymax = ry + rh
    
        return new_xmin, new_ymin, new_xmax, new_ymax
        

if __name__ == '__main__':
    
    file_path = r'G:/test/'  # input path end with /
    rotated_path = r'G:/test/rotate/'  # rotated path end with /
 
   
    for angle in [45,15]:
        for file in os.listdir(file_path):

            if file.endswith('.jpg'):
                a, b = os.path.splitext(file)
                # s=file_path + a + '.jpg'
                # img = cv2.imread(s)

                img=cv2.imdecode(np.fromfile(file_path + a + '.jpg',dtype=np.uint8),flags=-1)     
                rotated_img = rotate_img(img, angle)
                width_d = rotated_img.shape[1]
                height_d = rotated_img.shape[0]
                cv2.imencode('.jpg', rotated_img)[1].tofile(rotated_path + a + '_' + str(angle) + 'd.jpg')  

                # cv2.imwrite(rotated_path + a + '_' + str(angle) + 'd.jpg', rotated_img)

                print(str(file) + ' ' + 'has been rotated for' + " "+ str(angle) + ' degrees')

            if file.endswith('.xml'):
                src = cv2.imdecode(np.fromfile(file_path + a + '.jpg',dtype=np.uint8),flags=-1)
                tree = ET.parse(file_path + a + '.xml')
                root = tree.getroot()
                root.find('folder').text = 'rotated_img_xml'
                root.find('filename').text = a + '_' + str(angle) + 'd.jpg'
                root.find('path').text = rotated_path + a + '_' + str(angle) + 'd.jpg'
                root.find("size").find('width').text = str(width_d)
                root.find("size").find('height').text = str(height_d)
                
                for box in root.iter('bndbox'):
                    xmin = float(box.find('xmin').text)
                    ymin = float(box.find('ymin').text)
                    xmax = float(box.find('xmax').text)
                    ymax = float(box.find('ymax').text)
                    new_xmin, new_ymin, new_xmax, new_ymax = rotate_xml(src, xmin, ymin, xmax, ymax, angle)
                    box.find('xmin').text = str(max(new_xmin, 0))
                    box.find('ymin').text = str(max(new_ymin, 0))
                    box.find('xmax').text = str(min(new_xmax, width_d))
                    box.find('ymax').text = str(min(new_ymax, height_d))
                tree.write(rotated_path + a + '_' + str(angle) + 'd.xml')
                print(str(file) + ' ' + 'has been rotated for' + " "+str(angle) + ' degrees')