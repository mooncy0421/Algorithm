# https://www.acmicpc.net/problem/1931
import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# 회의가 빨리 끝나는 순으로 정렬, 같은 시간에 끝나는 회의가 있다면 더 빨리 시작하는 순서로 정렬
# 회의 중 (0,2), (2,2)가 있는 경우 시작 시간 기준 정렬 없다면 (2,2)가 앞에와서 (0,2)는 회의 못하는 것으로 인식되기 때문에
# 끝나는 순서로 정렬한 후 시작 순으로도 정렬해야함
meetings = sorted(meetings, key= lambda x: (x[1], x[0]))

cnt = 0
cur_end = 0
for start, end in meetings:
    # 현재 회의가 끝난 이후 시작하는 회의 중 시작시간 가장 빠른 것부터 선택
    if start >= cur_end:
        cur_end = end
        cnt += 1
print(meetings)
print(cnt)