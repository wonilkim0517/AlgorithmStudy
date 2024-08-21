import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0

for i in range(N):
    A_max = max(A)
    B_min = min(B)

    S += (A_max * B_min)

    A.remove(A_max)
    B.remove(B_min)

print(S)