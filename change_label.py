import os
path='G:\\image_datasets\\classify_recycle_data\\plastic_bottle\\labels'

for files in os.listdir(path):
    a=[]
    fo = open(path+"\\"+files, "r")
    for i in fo.readlines():
        a.append(i)
        # print(i)
        
    # print(a)
    fo.close()


    fo1=open(path+"\\"+files, "w")
    for i in range(len(a)):
        fo1.write("2")
        fo1.write(a[i][1:])
    fo1.close()
        