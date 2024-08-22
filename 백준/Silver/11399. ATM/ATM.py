import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()

current_count = 0
total_count = 0

for i in P:
    current_count += i
    total_count += current_count

print(total_count)