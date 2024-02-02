import sys

input = sys.stdin.readline

N, M = map(int, input().split())
elements = list(map(int, input().split()))
elements.sort()
s = []
visited = set()

def dfs(start):
    if len(s) == M:
        current_s = tuple(s)
        if current_s not in visited:
            visited.add(current_s)
            print(' '.join(map(str, s)))
        return
    for i in range(start, len(elements)):
        s.append(elements[i])
        dfs(i)
        s.pop()
dfs(0)
