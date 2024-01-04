# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:43:43 2021

@author: Liiv
"""

    
import random

#i = 0

num1 = num2 = num3 = 0

for i in range(6):
    num = random.randint(1,10)
    if i ==0:
        num1 == num
    elif i ==1:
        while num == num1:
            num = random.randint(1,10)
        else:
            num2 = num
    elif i ==2:
        while num == num1 or num == num2:
            num = random.randint(1,10)
        else:
            num3 = num
    elif i ==3:
        while num == num1 or num == num2 or num ==num3:
            num = random.randint(1,10)
        else:
            num4 = num
    elif i ==4:
        while num == num1 or num == num2 or num ==num3 or num ==num4:
            num = random.randint(1,10)
        else:
            num5 = num
    elif i ==5:
        while num == num1 or num == num2 or num ==num3 or num ==num4 or num ==num5:
            num = random.randint(1,10)
        else:
            num6 = num
    #i = i+1
print(num1,num2,num3,num4,num5,num6)
        
        
            
            

