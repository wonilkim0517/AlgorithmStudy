import sys
input = sys.stdin.readline

N=int(input())
ls = [int(i) for i in input().rstrip()]
print(sum(ls))