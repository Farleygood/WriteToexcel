#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

import random
import xlwt

# 创建一个工作薄
f = xlwt.Workbook()
# 创建一个工作表，命名为‘预约号’
sheet1 = f.add_sheet(u'预约号', cell_overwrite_ok=True)   ##第二参数用于确认同一个cell单元是否可以重设值。  
l = []
for i in range(100):
    j = random.randint(12340000,12349999)
    d = 'CM'+str(j)    #将数字转换成字符串，用CM拼接
    l.append(d)
# print '\n'.join(l)
# for n in range(100):
    sheet1.write(0,0,u'这是预约号')     #在第一行第一列写入标题
    sheet1.write(i+1,0,l[i])         #从第二行第一列开始，每行的第一列写入一个预约号码
f.save('test.xls')                   #一定要记得保存
     