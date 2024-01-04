# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:53:37 2022

@author: Ivan
"""

total = 0                               # 先將分數歸零   
count = 0                               # 先將輸入次數歸零
while True:
    print("第%d位同學"%(count+1))       # 輸入成績後輸入次數自動遞增1
    score = int(input("請輸入成績: "))
    total += score                     # total = total + score (總分 = 前回輸入分數與本回輸入分數加總後賦(予)值)
    count+=1                           # count = count + 1 (總輸入次數遞增1 = 前回輸入次數與本回輸入次數加總後賦(予)值)
    _quit = input("是否離開(y/n)?: ")
    if _quit == "y" or _quit == "Y":
        break
    else:
        continue
print("共輸入{}位同學成績,總分={},總平均={}".format(count,total,round(total/count,2)))

    
