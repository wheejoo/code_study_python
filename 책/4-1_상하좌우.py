# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:49:53 2020

@author: wheejoo
"""

"""
n = 5 plans = RRRUDD
"""
n = int(input())
x, y = 1, 1 #현재위치
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny
    
print(x, y)