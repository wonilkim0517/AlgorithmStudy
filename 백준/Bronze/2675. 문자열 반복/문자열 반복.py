import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num, alpha = input().split()
    num = int(num)
    alpha = str(alpha)

    for i in range(len(alpha)):
        print(num * alpha[i], end='')
    print()
