from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x1, y1, x2, y2, l):
    q = deque()
    q.append((x1, y1))
    visited = [[0] * l for _ in range(l)]
    visited[x1][y1] = 1

    while q:
        cx, cy = q.popleft()
        if cx == x2 and cy == y2:
            return visited[cx][cy] - 1

        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
    return -1

for _ in range(n):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    print(bfs(x1, y1, x2, y2, l))