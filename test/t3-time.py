#!/usr/bin/env python
# encoding: utf-8

print '设置时间'
year = raw_input("输入年(四位整数):")
year = str(int(year))
print year + '年'
month = raw_input("输入月份(1~12):")
print year + '年' + month + '月'
date = raw_input("输入日期(1~31):")
print year + '年' + month + '月' + date +'日'
hour = raw_input("输入小时(1~24):")
print year + '年' + month + '月' + date +'日'+ hour + '点'
second = raw_input("输入分(0~59):")
print year + '年' + month + '月' + date +'日'+ hour + '点' + second+ '分'
date_set = "\"" + year + "-" + month.zfill(2) + "-" + date.zfill(2) + " " + hour.zfill(2) + ":" + second.zfill(2) +":00\""
print date_set