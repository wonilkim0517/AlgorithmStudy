from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
answer = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    bfs(i)
    answer.append(sum(visited))

print(answer.index(min(answer)) + 1)
