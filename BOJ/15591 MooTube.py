# https://www.acmicpc.net/problem/15591
import sys
from collections import defaultdict
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
USADO = defaultdict(list)   # Adjacent List with USADO

for _ in range(N-1):
    p, q, usa = map(int, sys.stdin.readline().split())
    USADO[p].append([q, usa])
    USADO[q].append([p, usa])

for _ in range(Q):
    K, V = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(N+1)]
    visited[V] = True
    cnt = 0
    que = deque([V])
    while que:
        current = que.popleft()
        for nxt, usa in USADO[current]:
            if usa >= K and not visited[nxt]:
                que.append(nxt)
                visited[nxt] = True
                cnt += 1
    print(cnt)