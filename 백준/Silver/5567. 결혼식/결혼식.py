import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    global cnt
    q = deque([(start, 0)])
    visited[start] = True
    while q:
        x, depth = q.popleft()
        if depth>=2:
            continue
        for i in graph[x]:
            if not visited[i]:
                q.append((i, depth + 1))
                visited[i] = True
                cnt += 1
    return cnt

print(bfs(1))