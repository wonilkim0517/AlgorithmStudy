import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
K -= 1

stack = []
q = deque()

for i in range(1, N + 1):
    q.append(i)

while q:
    q.rotate(-K)
    stack.append(q.popleft())

print(str(stack).replace('[', '<').replace(']', '>'))
