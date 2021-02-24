# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:32:33 2020

@author: wheejoo
"""

n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_v = min(data)
    result = max(result, min_v)
    
print(result)
    
# print(d)
# print(d[0])
# print(d[1])
# print(d[2])

# first = min(d[0])
# second = min(d[1])
# third = min(d[2])

