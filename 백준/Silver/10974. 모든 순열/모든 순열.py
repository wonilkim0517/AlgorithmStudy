import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
elements = [i + 1 for i in range(N)]
permutationsList = list(permutations(elements))

for permutationsPrint in permutationsList:
    print(*permutationsPrint)
