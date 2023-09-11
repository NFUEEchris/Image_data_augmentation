import cv2
import numpy as np
import os 
import shutil
# 讀取影像
img_dir='C:\code\data\img'
xml_dir='C:\\code\\data\\annotation'

exposure = 1.5  # 調整曝光的倍數，大於1增加曝光，
exposure_ = 0.5 # 小於1減少曝光
def is_image_file(file_path):
    # 定義支援的圖片擴展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    # 獲取文件的擴展名
    _, file_extension = os.path.splitext(file_path)

    # 將擴展名轉換為小寫並檢查是否在支援的圖片擴展名列表中
    return file_extension.lower() in image_extensions

for i in os.listdir(img_dir):
    filename,extension = os.path.splitext(i)
    path=os.path.join(img_dir,i)
    if is_image_file(path)==True:
        image = cv2.imread(path)
        # 乘以曝光值以調整曝光
        adjusted_image_p = cv2.multiply(image, np.array([exposure]))

        # 將調整後的像素值限制在0到255之間
        adjusted_image_p = np.clip(adjusted_image_p, 0, 255)

        # 將浮點數像素值轉換為8位整數
        adjusted_image_p = adjusted_image_p.astype(np.uint8)

        adjusted_image_n = cv2.multiply(image, np.array([exposure_]))

        # 將調整後的像素值限制在0到255之間
        adjusted_image_n = np.clip(adjusted_image_n, 0, 255)

        # 將浮點數像素值轉換為8位整數
        adjusted_image_n = adjusted_image_n.astype(np.uint8)
        # 顯示原始和調整後的影像
        # cv2.imshow('Original Image', image)
        # cv2.imshow('Adjusted Image', adjusted_image_p)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 保存調整後的影像
        shutil.copy(os.path.join(xml_dir,filename + '.xml'),os.path.join(xml_dir,'br_' + filename + '.xml'))
        cv2.imwrite(os.path.join(img_dir,'br_'+i), adjusted_image_p)
        shutil.copy(os.path.join(xml_dir,filename + '.xml'),os.path.join(xml_dir,'dr_' + filename + '.xml'))
        cv2.imwrite(os.path.join(img_dir,'dr_'+i), adjusted_image_n)

        # print(i)






