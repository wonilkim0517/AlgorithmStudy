import sys

input = sys.stdin.readline

N = int(input())
rope_list = []

for _ in range(N):
    rope = int(input())
    rope_list.append(rope)

rope_list.sort(reverse=True)
max_weight = 0

for i in range(N):
    max_weight = max(max_weight, rope_list[i] * (i+1))

print(max_weight)
