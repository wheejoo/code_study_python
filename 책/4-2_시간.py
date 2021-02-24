# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:57:08 2020

@author: wheejoo
"""

"""
h = 5
"""

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                # print(str(i) + str(j) + str(k))
                count += 1
                
print(count)