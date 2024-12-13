import heapq
import sys

input = sys.stdin.readline

list = []
N = int(input())
for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(list, -x)
    else:
        if len(list) == 0:
            print(0)
        else:
            print(-heapq.heappop(list))
