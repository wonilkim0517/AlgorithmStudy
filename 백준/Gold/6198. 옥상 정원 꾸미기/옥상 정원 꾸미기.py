import sys

input = sys.stdin.readline

N = int(input())

buildings = []
stack = []
result = 0

for _ in range(N):
    n = int(input())
    buildings.append(n)

for i in range(N):
    while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()

    result += len(stack)  

    stack.append(i)

print(result)