import sys

input = sys.stdin.readline

N = int(input())
nSet = set(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))

for num in mList:
    if num in nSet:
        print(1)
    else:
        print(0)
