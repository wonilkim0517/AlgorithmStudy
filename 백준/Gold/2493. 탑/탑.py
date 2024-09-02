import sys

input = sys.stdin.readline

N = int(input())

tower = list(map(int, input().split()))
razer = [0] * N
stack = []

for i in range(N):
    while stack and tower[stack[-1]] <= tower[i]:
        stack.pop()

    if stack:
        razer[i] = stack[-1] + 1

    stack.append(i)

print(' '.join(map(str, razer)))