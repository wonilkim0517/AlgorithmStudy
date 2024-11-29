import sys

input = sys.stdin.readline

K, N = map(int, input().split())
LANLines = []
for _ in range(K):
    LANLines.append(int(input()))

start, end = 1, max(LANLines)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for LANLine in LANLines:
        sum += LANLine // mid

    if sum < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)