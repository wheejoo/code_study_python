# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:22:33 2020

@author: wheejoo
"""

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v,e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
cycle = False
    
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('cycle 발생')
else:
    print('nothing')