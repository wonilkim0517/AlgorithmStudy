from collections import deque
import sys

MAX_NUM = 50
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
answer = []

while True:
    A, B = map(int, input().split())
    if A == -1 and B == -1:
        break
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1] * (N + 1)
    visited[start] = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[n] + 1
    return max(visited[1:])

for i in range(1, N + 1):
    answer.append(bfs(i))

min_answer = min(answer)
president_count = answer.count(min_answer)
print(f'{min_answer} {president_count}')

for i in range(N):
    if answer[i] == min_answer:
        print(i + 1, end=' ')