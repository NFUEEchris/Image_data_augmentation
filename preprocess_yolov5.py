import os ,sys
import random
import shutil

file="G:\\image_datasets\\classify_recycle_data\\train"   #will create file all_train,all_test in upper folder
train_rate,val_rate=0.8,0.1
dir_file=os.listdir(file)
jpg_list=[]
txt_list=[]
# print(dir_file)
# print(os.path.join(file, os.pardir))
train_file=os.path.join(file, os.pardir,"all_train")
val_file=os.path.join(file, os.pardir,"all_val")
test_file=os.path.join(file, os.pardir,"all_test")
# print(train_file)

# create file if it's not exist
if os.path.isdir(train_file)==0:
    os.mkdir(train_file)
if os.path.isdir(test_file)==0:
    os.mkdir(test_file)
if os.path.isdir(val_file)==0:
    os.mkdir(val_file)

for i in range(len(dir_file)):
    # print(dir_file[i])
    if "jpg" in dir_file[i]:
        jpg_list.append(dir_file[i])
    elif "txt" in dir_file[i]:
        txt_list.append(dir_file[i])

#shuffle       
random.shuffle(jpg_list)
train_set=set(jpg_list[0:int(len(jpg_list)*train_rate)])
val_set=set(jpg_list[int(len(jpg_list)*train_rate):int(len(jpg_list)*(train_rate+val_rate))])
#diff
test_set=set(jpg_list)-train_set-val_set
#covert set to list   
train_list=list(train_set)
val_list=list(val_set)
test_list=list(test_set)

# print(os.path.join(file,train_list[1]))
# print(os.path.join(train_file,train_list[1]))


for i in train_list:
    shutil.copyfile(os.path.join(file,i),os.path.join(train_file,i))
    filename=os.path.splitext(i)[0]+".txt" #name
    txt_file=os.path.join(file,filename)
    if os.path.exists(txt_file):
        shutil.copyfile(txt_file,os.path.join(train_file,filename))
    else:
        print(filename)

for i in test_list:
    shutil.copyfile(os.path.join(file,i),os.path.join(test_file,i))
    filename=os.path.splitext(i)[0]+".txt"#name
    # print(filename)
    txt_file=os.path.join(file,filename)
    # print(txt_file)
    if os.path.exists(txt_file):
        shutil.copyfile(txt_file,os.path.join(test_file,filename))
    else:
        print(filename)

for i in val_list:
    shutil.copyfile(os.path.join(file,i),os.path.join(val_file,i))
    filename=os.path.splitext(i)[0]+".txt"#name
    # print(filename)
    txt_file=os.path.join(file,filename)
    # print(txt_file)
    if os.path.exists(txt_file):
        shutil.copyfile(txt_file,os.path.join(val_file,filename))
    else:
        print(filename)
##------bread
##  |-----all_train(sort result)
##  |-----all_test(sort result)
##  |-----croissant(set file here,include image and label file (.txt))
##  |-----french bread(set file here,include image and label file (.txt))
##   *  
##   *  
##   *  
