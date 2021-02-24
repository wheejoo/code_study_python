# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:08:33 2020

@author: wheejoo
"""

from collections import deque
import heapq

def solution(n, exec_times):
    queue = deque(exec_times)
    
    FINISHED_AT, SERVER_ID, JOBS_DONE = 0,1,2   
    servers = [[0, i, 0] for i in range(n)]
    heapq.heapify(servers)
    
    while queue:
        target_server = heapq.heapify(servers[SERVER_ID])
        target_server[FINISHED_AT] += queue.popleft()
        target_server[JOBS_DONE] += 1
        heapq.heapify(target_server)
        
    servers.sort(key=lambda x: x[SERVER_ID])
    return [server[JOBS_DONE] for server in servers]

servers = [[0, i, 0] for i in range(5)]
print(servers)
    
