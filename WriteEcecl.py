#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Administrator'

f = xlwt.Workbook()
sheet1 = f.add_sheet(u'预约号', cell_overwrite_ok=True)
l = []
for i in range(100):
    j = random.randint(12340000,12349999)
    d = 'CM'+str(j)
    l.append(d)
# print '\n'.join(l)

for n in range(100):
    sheet1.write(0,0,u'这是预约号')
    sheet1.write(n+1,0,l[n])
f.save('test.xls')
     