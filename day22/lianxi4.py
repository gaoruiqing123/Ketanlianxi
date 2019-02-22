#创建文件夹
import os
#os.mkdir('E://exma_22')
#创建文件
import random
a=open('E://exma_22/zuoye.txt','w')
for i in range(10):
    a.write(str(random.randint(0,100))+'\n')

b = open('E://exma_22/zuoye.txt','r')
print(str(b.read(10)))