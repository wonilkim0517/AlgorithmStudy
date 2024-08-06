import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(N):
        if nums[j] == 1:
            graph[i].append(j)

def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)