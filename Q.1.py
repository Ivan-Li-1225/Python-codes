# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:23:36 2023

@author: ahc60
"""

num_rows = int(input("請輸入行數 : "))

for i in range(1,num_rows + 1):
    print("\n")
    for k in range(i,num_rows + 1):
        print(" ", end=" ")
    for j in range(i):
        print(" ","*", end=" ")
        
        