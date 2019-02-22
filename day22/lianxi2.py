# .在1中的文件夹“exam-6”下创建一个python.txt文件，
# 并依次向其中写入下述内容：（40分）
# 1)Python的六大基本数据类型
# 2)列举3个学过的Python模块，每个模块下各列举两个常用的方法

import os
#写文件
f=open('E://exam-6/python.txt','w')
list = ['Number','String','Tuple','List','Stes','Dictionary']
for i in range(len(list)):
    f.write(list[i]+'\n')
    f.newlines
    f.flush()
