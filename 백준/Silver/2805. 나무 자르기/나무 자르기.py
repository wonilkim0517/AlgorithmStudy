import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)