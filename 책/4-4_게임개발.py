# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:18:50 2020

@author: wheejoo
"""
# 4*4 입력받기
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

x, y , direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문 처리

#전체 맵 정보 입력받기 
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #가보지 않은 곳
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(count)
        