import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

tomatoes = []
visited = [[0] * M for _ in range(N)]

for _ in range(N):
    tomatoes.append(list(map(int, input().split())))

def bfs():
    days = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1

    while q:
        for _ in range(len(q)):
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and tomatoes[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        tomatoes[nx][ny] = 1
        days += 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and tomatoes[i][j] == 0:
                return -1
    return days - 1

print(bfs())