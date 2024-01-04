# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 09:06:37 2022

@author: Ivan
"""

list1 = ['陳大元',98,100,89,
         '王曉明',68,90,79,
         '謝晶燕',78,88,78,
	     '愛怡良',100,100,79,
	     '周小星',85,95,75]

list2 = [
	['陳大元',98,100,89],
	['王曉明',68,90,79],
	['謝晶燕',78,88,78],
	['愛怡良',100,100,79],
	['周小星',85,95,75]
]


# print(list1[0])     # Ans=>陳大元
# print(list2[0])     # Ans=>['陳大元',98,100,89]
# print(list2[0][0])  # Ans=>陳大元
# print(list2[1][1])  # Ans=>68
# print(list2[2][3])  # Ans=>78
# print(list2[4][4])  # over range

# for迴圈取值

# for i in range(len(list2)):
#     for j in range(len(list2[i])):
#         print(list2[i][j])
        
# 加入成績總分
for i in range(len(list2)):
    total = list2[i][1] + list2[i][2] + list2[i][3]
    list2[i].append(total)
    for j in range(len(list2[i])):
        print(list2[i][j])
print()
        
# 加入平均分/總平均分

for i in range(len(list2)):
    avg = round((list2[i][1] + list2[i][2] + list2[i][3]) / 3)
    list2[i].append(avg)
    for j in range(len(list2[i])):
        print(list2[i][j])
avg_t = 0
for i in range(len(list2)):
    avg_t += list2[i][5]
print("總平均分數=", avg_t / len(list2))
