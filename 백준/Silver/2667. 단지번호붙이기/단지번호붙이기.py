from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
squareMap = []
visited = [[0] * N for _ in range(N)]
for _ in range(N):
    squareMap.append(list(map(int, input().rstrip())))

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
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if squareMap[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    area += 1

    return area

areas = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and squareMap[i][j] == 1:
            areas.append(bfs(i, j))

areas.sort()
print(len(areas))
for area in areas:
    print(area)
