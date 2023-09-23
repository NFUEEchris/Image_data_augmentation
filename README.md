# Image_data_augmentation
### warning !!!!warning !!!warning !!!
#### label 僅限 xml (label only xml file)

## check_imgnlabel (delete warning).py

#### 確認 labels 與 images 是否有相應的檔案
#### (check is labels and images match or not) 

## cut2half.py
#### 將照片切成兩半
#### (cut images to half and output)

## flip(including label).py
#### 將 images 與 labels 翻轉，用於資料擴增
#### (flip images and labels)

## light_enhance.py
#### 針對圖片亮度調整，label是原圖的label，用於資料擴增
#### (images light enhance，will generate label xml files same as origanal xml file)

## rotated_label.py
#### 將 images 與 labels 旋轉，用於資料擴增
#### (rotate the images and labels)

## set_name2txt.py
#### 改測試文件名的 test.txt，用於更改測試內容
#### (change the yolo test.txt)

## txt2xml.py
#### 將txt 檔轉成 xml檔
#### (convert labeling txt file to xml file)

## video_to_frames.py and  videocap.py
#### 將影片的每幀儲存成照片
#### (split video to frames)

## xml2txt.py
#### 將xml 檔轉成 txt檔
#### (convert labeling xml file to txt file)
