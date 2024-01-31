import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
elements = list(map(int, input().split()))
elements.sort()

permutationsList = list(permutations(elements, M))

for permutationsPrint in permutationsList:
    print(' '.join(map(str, permutationsPrint)))
