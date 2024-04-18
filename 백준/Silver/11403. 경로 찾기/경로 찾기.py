import sys

input = sys.stdin.readline

N = int(input())

graph = [[0] * N for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

visited = graph

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                visited[i][j] = 1

for i in range(N):
    for j in range(N):
        if j == (N - 1):
            print(visited[i][j])
        else:
            print(visited[i][j], end=' ')