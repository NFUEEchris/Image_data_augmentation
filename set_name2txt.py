import os 

with open('test4.txt', 'w') as file:
    for i in range(11718,11808):
        text='vannamei'+str(i)
        file.write(text)
        file.write('\n')    
