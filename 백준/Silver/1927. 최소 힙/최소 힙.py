import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(nums, x)
    elif x == 0:
        if nums:
            print(heapq.heappop(nums))
        else:
            print(0)
    


