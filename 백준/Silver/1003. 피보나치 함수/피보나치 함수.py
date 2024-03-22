import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    count0 = [1, 0]
    count1 = [0, 1]
    N = int(input())
    if N <= 40:
        for j in range(2, N + 1):
            count0.append(count0[j - 2] + count0[j - 1])
            count1.append(count1[j - 2] + count1[j - 1])
        print(f'{count0[N]} {count1[N]}')