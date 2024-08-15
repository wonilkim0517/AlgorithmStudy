from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[n] + 1
    return visited

distance = bfs(1)

max_distance = max(distance)
fastest_barn = distance.index(max(distance))
cnt_max_distance = distance.count(max(distance))

print(f'{fastest_barn} {max_distance} {cnt_max_distance}')