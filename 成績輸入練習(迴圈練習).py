# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 08:58:28 2022

@author: Ivan
"""

print("---歡迎使用學生成績輸入系統---")

stud_1 = input("請輸入第一位學生姓名: ")
score_1 = int(input("請輸入第一位學生成績(0~100): "))
while True:
    if (score_1 >= 0) and (score_1 <= 100):
        break
    else:
        print("\a輸入錯誤, 請重新輸入!")
        score_1 = int(input("請輸入第一位學生成績(0~100): "))
        continue
   
stud_2 = input("請輸入第二位學生姓名: ")
score_2 = int(input("請輸入第二位學生成績(0~100): "))
while True:
    if (score_2 >= 0) and (score_2 <= 100):
        break
    else:
        print("\a輸入錯誤, 請重新輸入!")
        score_2 = int(input("請輸入第二位學生成績(0~100): "))
        continue
        
stud_3 = input("請輸入第三位學生姓名: ")
score_3 = int(input("請輸入第三位學生成績(0~100): "))
while True:
    if (score_3 >= 0) and (score_3 <= 100):
        break
    else:
        print("\a輸入錯誤, 請重新輸入!")
        score_3 = int(input("請輸入第三位學生成績(0~100): "))
        continue

score_total = score_1 + score_2 + score_3
score_avg = (score_total / 3)
print("姓名","成績",sep="   ")
print("%s %5d"%(stud_1,score_1),"\n%s %6d"%(stud_2,score_2),"\n%s %8d"%(stud_3,score_3))
print("總分為:%d 平均分為:%6.2f"%(score_total,score_avg))