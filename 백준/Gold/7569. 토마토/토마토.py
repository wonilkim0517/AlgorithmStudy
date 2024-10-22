import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = [[[0] * H for _ in range(N)] for _ in range(M)]
for h in range(H):
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            tomato[m][n][h] = row[m]

visited = [[[0] * H for _ in range(N)] for _ in range(M)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    q = deque()

    for m in range(M):
        for n in range(N):
            for h in range(H):
                if  tomato[m][n][h] == 1:
                    q.append((m, n, h))
                    visited[m][n][h] = 1

    while q:
        cx, cy, cz = q.popleft()
        for i in range(6):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if not visited[nx][ny][nz] and tomato[nx][ny][nz] == 0:
                    q.append((nx, ny, nz))
                    visited[nx][ny][nz] = visited[cx][cy][cz] + 1
                    tomato[nx][ny][nz] = 1

bfs()

max_days = 0
all_ripe = True

for m in range(M):
    for n in range(N):
        for h in range(H):
            if tomato[m][n][h] == 0:
                all_ripe = False
            max_days = max(max_days, visited[m][n][h] - 1)

if not all_ripe:
    print(-1)
else:
    print(max_days)
