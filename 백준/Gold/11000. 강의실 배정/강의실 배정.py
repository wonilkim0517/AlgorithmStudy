import sys
import heapq

input = sys.stdin.readline

N = int(input())
classes = []
result = 0

for _ in range(N):
    classes.append(list(map(int, input().split())))

classes.sort()

end_times = []
heapq.heappush(end_times, classes[0][1])

for i in range(1, N):
    S, T = classes[i]

    if end_times[0] <= S:
        heapq.heappop(end_times)

    heapq.heappush(end_times, T)

result = len(end_times)
print(result)
