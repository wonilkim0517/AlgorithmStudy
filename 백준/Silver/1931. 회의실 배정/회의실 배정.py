import sys

input = sys.stdin.readline

N = int(input())
room = []

for _ in range(N):
    start, end = map(int, (input().split()))
    room.append([start, end])

room.sort(key=lambda x: (x[1], x[0]))

finish = 0
count = 0

for i, j in room:
    if i >= finish:
        count += 1
        finish = j

print(count)
