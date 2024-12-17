import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
mapWithWalls = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    mapWithWalls.append(list(map(int, input().strip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0, 1))
    visited[0][0][0] = 1

    while q:
        cx, cy, broken, distance = q.popleft()

        if cx == N - 1 and cy == M - 1:
            return distance

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 없는 곳
                if not visited[nx][ny][broken] and mapWithWalls[nx][ny] == 0:
                    q.append((nx, ny, broken, distance + 1))
                    visited[nx][ny][broken] = 1

                # 벽이 있는 곳
                elif not visited[nx][ny][1] and mapWithWalls[nx][ny] == 1 and broken == 0:
                    q.append((nx, ny, 1, distance + 1))
                    visited[nx][ny][1] = 1
    return -1

print(bfs())

