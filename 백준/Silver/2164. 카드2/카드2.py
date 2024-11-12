import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
nums = deque()

for i in range(1, N + 1):
    nums.append(i)

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(*nums)
