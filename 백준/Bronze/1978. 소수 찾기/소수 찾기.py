import sys

input = sys.stdin.readline

N = int(input())
numberList = list(map(int, input().split()))
answer = 0

for i in range(N):
    cnt = 1
    for j in range(2, numberList[i] + 1):
        if numberList[i] % j == 0:
            cnt += 1
    if cnt == 2:
        answer += 1
print(answer)
