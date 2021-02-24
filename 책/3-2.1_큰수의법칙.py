# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:14:09 2020

@author: wheejoo
"""

n,m,k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        # print(result)
        m -= 1
        
    if m == 0:
        break
    result += second
    # print(result)
    m -= 1
    
print(result)
# n = 5
# a = [2, 4, 5, 4, 6]
# a.sort()
# print(a[n-1])
# print(a[n-2])