from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph= [[] for _ in range(N + 1)]
cnt = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    count = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                count += 1
    return count

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    cnt.append(bfs(i))

for i in range(N):
    if cnt[i] == max(cnt):
        print(i + 1, end = ' ')