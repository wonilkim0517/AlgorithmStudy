from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(str, input())))

RGB_RG = [row[:] for row in RGB]
for i in range(N):
    for j in range(N):
        if RGB_RG[i][j] == 'G':
            RGB_RG[i][j] = 'R'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, grid, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    color = grid[x][y]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


visited_normal = [[0] * N for _ in range(N)]
count_normal = 0
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            bfs(i, j, RGB, visited_normal)
            count_normal += 1

visited_colorBlind = [[0] * N for _ in range(N)]
count_colorBlind = 0
for i in range(N):
    for j in range(N):
        if not visited_colorBlind[i][j]:
            bfs(i, j, RGB_RG, visited_colorBlind)
            count_colorBlind += 1

print(count_normal, count_colorBlind)