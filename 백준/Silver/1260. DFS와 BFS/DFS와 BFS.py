import sys
from collections import deque

input = sys.stdin.readline


def dfs(c):
    ans_dfs.append(c)
    visited_dfs[c] = True

    for n in graph[c]:
        if not visited_dfs[n]:
            dfs(n)


def bfs(s):
    q = deque([s])
    ans_bfs.append(s)
    visited_bfs[s] = True

    while q:
        c = q.popleft()

        for n in graph[c]:
            if not visited_bfs[n]:
                q.append(n)
                ans_bfs.append(n)
                visited_bfs[n] = True


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

visited_dfs = [False] * (N + 1)
ans_dfs = []
dfs(V)

visited_bfs = [False] * (N + 1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
