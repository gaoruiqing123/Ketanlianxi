#传文件夹
import os
import random
#os.mkdir('E://abcd_22')
#创建文件
a=open('E://abcd_22/adbc.txt','w')
#写数据
str ='adasgufkashflasihfoadjg;sdgjhiuhgnlaskfvhosdhflsodm'
for i in range(100):
    a.write(random.choice(str)+'\n')

#读文件数据

b = open('E://abcd_22/adbc.txt','r')
c = b.read(1000)
print(c)
