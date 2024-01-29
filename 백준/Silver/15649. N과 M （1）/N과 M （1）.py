import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

elements = [i + 1 for i in range(N)]
permutationList = list(permutations(elements, M))

for permutationsPrint in permutationList:
    print(' '.join(map(str, permutationsPrint)))
