import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

drawingPaper = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    drawingPaper.append(list(map(int, input().split())))

count = 0
max_area = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    area = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and drawingPaper[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    area += 1
    return area

for i in range(n):
    for j in range(m):
        if drawingPaper[i][j] and not visited[i][j]:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)
