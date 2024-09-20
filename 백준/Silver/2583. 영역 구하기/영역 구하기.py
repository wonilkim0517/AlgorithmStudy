import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

graphPaper = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graphPaper[i][j] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    area = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and graphPaper[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    area += 1
    return area

areas = []

for i in range(M):
    for j in range(N):
        if not visited[i][j] and graphPaper[i][j] == 0:
            areas.append(bfs(i, j))

areas.sort()
print(len(areas))
print(" ".join(map(str, areas)))