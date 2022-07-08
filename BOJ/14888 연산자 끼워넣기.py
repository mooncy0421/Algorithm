# https://www.acmicpc.net/problem/14888
import sys

N = int(sys.stdin.readline())   # 숫자 갯수, 연산자 갯수 + 1
nums = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split())) # + - * /

max_val = -float('inf')
min_val = float('inf')

def dfs(num_oper, res, plus, minus, mul, div):
    global max_val, min_val
    # 모든 연산자 다 사용시 최대, 최소값 조정
    if num_oper == N:
        max_val = max(res, max_val)
        min_val = min(res, min_val)
        return
    # 각 연산자 남은 경우에 따라 DFS 수행
    if plus:
        dfs(num_oper+1, res+nums[num_oper], plus-1, minus, mul, div)
    if minus:
        dfs(num_oper+1, res-nums[num_oper], plus, minus-1, mul, div)
    if mul:
        dfs(num_oper+1, res*nums[num_oper], plus, minus, mul-1, div)
    if div:
        dfs(num_oper+1, int(res/nums[num_oper]), plus, minus, mul, div-1)

dfs(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(max_val)
print(min_val)