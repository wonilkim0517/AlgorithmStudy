import sys

input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

s.sort(key=lambda x: (x[0], x[1]))

for x, y in s:
    print(x, y)
