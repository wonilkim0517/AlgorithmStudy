import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
region = []
for _ in range(N):
    region.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, height):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    area = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if region[nx][ny] > height and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    area += 1
    return area

areas = []

for height in range(101):
    visited = [[0] * N for _ in range(N)]
    area_count = 0

    for i in range(N):
        for j in range(N):
            if region[i][j] > height and not visited[i][j]:
                bfs(i, j, height)
                area_count += 1

    areas.append(area_count)
print(max(areas))