# https://www.acmicpc.net/problem/18428
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N = int(sys.stdin.readline())
students = []
teachers = []
hallway = []
school_map = []
for i in range(N):
    row = list(map(str, sys.stdin.readline().split()))
    for k in range(N):
        if row[k] == 'S':
            students.append([i,k])
        elif row[k] == 'T':
            teachers.append([i,k])
        else: hallway.append([i,k])
    school_map.append(row)

def search():
    que = deque(teachers)
    while que:
        t_r, t_c = que.popleft()
        for i in range(4):
            t_r_temp, t_c_temp = t_r, t_c
            while True:
                nt_r, nt_c = t_r_temp+dr[i], t_c_temp+dc[i]
                if 0 <= nt_r < N and 0 <= nt_c < N:
                    if temp_school_map[nt_r][nt_c] == 'S':
                        return False
                    elif temp_school_map[nt_r][nt_c] == 'O':
                        break
                else:
                    break
                t_r_temp, t_c_temp = nt_r, nt_c
    return True

res = 'NO'
obj_loc = list(combinations(hallway, 3))
for locs in obj_loc:
    temp_school_map = deepcopy(school_map)
    for r, c in locs:
        temp_school_map[r][c] = 'O'
    if search():
        res = 'YES'
        break
print(res)