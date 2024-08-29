import sys

input = sys.stdin.readline

N = int(input())
lines = []
result = 0

for _ in range(N):
    lines.append(list(map(int, input().split())))

lines.sort()

start, end = lines[0]

for i in range(1, N):
    x, y = lines[i]

    if x <= end:
        end = max(y, end)
    else:
        result += (end - start)
        start, end = x, y

result += (end - start)
print(result)
