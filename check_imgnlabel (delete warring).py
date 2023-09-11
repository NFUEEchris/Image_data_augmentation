import os
import glob
import shutil

label_path='C:\code\yolov7-pytorch-master\VOCdevkit\VOC2007\Annotations'
image_path='C:\code\yolov7-pytorch-master\VOCdevkit\VOC2007\JPEGImages'
data_img_path='C:\code\yolov7-pytorch-master\VOCdevkit\VOC2007\JPEGImages'
data_ann_path='C:\code\yolov7-pytorch-master\VOCdevkit\VOC2007\Annotations'
# image_path='C:\code\data augmention'
# label_path='C:\code\data augmention'
label_list=os.listdir(label_path)
image_list=os.listdir(image_path)
# print(glob.glob(os.path.join(image_path,"*.jpg")))
# print(glob.glob(os.path.join(label_path,"*.xml")))
# a='00001989.xml'
# print(os.path.splitext(a)[0])

def is_image_file(file_path):
    # 定義支援的圖片擴展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    # 獲取文件的擴展名
    _, file_extension = os.path.splitext(file_path)

    # 將擴展名轉換為小寫並檢查是否在支援的圖片擴展名列表中
    return file_extension.lower() in image_extensions

def is_xml_file(file_path):
    # 定義支援的圖片擴展名
    xml_extensions = ['.xml']

    # 獲取文件的擴展名
    _, file_extension = os.path.splitext(file_path)

    # 將擴展名轉換為小寫並檢查是否在支援的圖片擴展名列表中
    return file_extension.lower() in xml_extensions

# count=0
# for i in image_list:
#     filename,extension = os.path.splitext(i)
#     path=os.path.join(image_path,i)
#     b=os.path.join(label_path,filename+".xml")
#     if is_image_file(path) and os.path.exists(path) and  is_xml_file(b) and os.path.exists(b): 
#         # print("a")
#         # print(b)
#         # print("pic avaliable,annotation non-avaliable:" , i ," deleted")
#         if os.path.isfile(b)==0:
#             # os.remove(path) # just find pls comment
#             print("pic avaliable,annotation non-avaliable:" , i ," deleted")
#     else:
#         print(filename+'.jpg exsit ' +filename+'.xml not exsit')
#         shutil.copy(os.path.join(data_ann_path,filename+'.xml'),os.path.join(label_path,filename+'.xml'))
#         count+=1
#         # os.remove(os.path.join(image_path,i))
#         # print(os.path.join(image_path,i)," removed")
#         # print("miss "+filename+".xml")
# print(count)
count=0
for j in label_list:
    filename,extension = os.path.splitext(j)
    b=os.path.join(image_path,filename+".jpg")
    path=os.path.join(label_path,j)
    
    if is_xml_file(path) and os.path.exists(path) and  is_image_file(b) and os.path.exists(b):
        #jpg or png need change if need it
        # print(b)
        # print("pic non-avaliable,annotation avaliable:" , j ," deleted") 
        if os.path.isfile(b)==0:
            # os.remove(path) # just find pls comment
            print("pic non-avaliable,annotation avaliable:" , j ," deleted")
    else:
        os.remove(os.path.join(label_path,j))
        count+=1
        print(filename+'.xml exsit ' +filename+'.jpg not exsit' )
        # shutil.copy(os.path.join(data_img_path,filename+'.jpg'),os.path.join(image_path,filename+'.jpg'))
        #  print("miss "+filename+".jpg")
print(count)