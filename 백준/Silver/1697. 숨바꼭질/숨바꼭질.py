import sys
from collections import deque

input = sys.stdin.readline

NUM = 100000
N, K = map(int, input().split())

visited = [0] * (NUM + 1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        n = q.popleft()

        if n == K:
            return visited[n] - 1

        if n -1 >= 0 and not visited[n - 1]:
            q.append(n - 1)
            visited[n - 1] = visited[n] + 1


        if n + 1 <= NUM and not visited[n + 1]:
            q.append(n + 1)
            visited[n + 1] = visited[n] + 1

        if n * 2 <= NUM and not visited[n * 2]:
            q.append(n * 2)
            visited[n * 2] = visited[n] + 1

print(bfs(N))


