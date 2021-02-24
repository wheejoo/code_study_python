# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 01:06:08 2020

@author: wheejoo
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1
#     # print(count[array[i]])
    
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end = ' ')

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')