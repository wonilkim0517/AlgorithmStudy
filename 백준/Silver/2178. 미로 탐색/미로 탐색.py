import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))

visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    distance = [[0] * M for _ in range(N)]
    distance[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0<= ny < M:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy] + 1

                    if nx == N - 1 and ny == M - 1:
                        return distance[nx][ny]

print(bfs(0,0))