# 3.将1中创建的文档temp1.txt重命名为num.txt，
# 并生成20个0到100之内的随机数，
# 将这20个随机数写入num.txt文件，每行一个数。（40分）

#文件重命名
import os
import random
#重命名时前后必须路径必须一致
#os.rename('E://exam-6/temp1.txt','E://exam-6/num.txt')
#打开文件
a = open('E://exam-6/num.txt','w')
for i in range(20):
    a.write(str(random.randint(0,100))+'\n')

b = open('E://exam-6/python.txt','r')
print(b.read(100))
