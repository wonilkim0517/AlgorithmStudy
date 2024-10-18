import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

startLink = []
visited = [0] * (F + 1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        n = q.popleft()

        if n == G:
            return visited[n] - 1

        if n + U <= F and not visited[n + U]:
            q.append(n + U)
            visited[n + U] = visited[n] + 1

        if n - D > 0 and not visited[n - D]:
            q.append(n - D)
            visited[n -D] = visited[n] + 1

    return "use the stairs"

print(bfs(S))
