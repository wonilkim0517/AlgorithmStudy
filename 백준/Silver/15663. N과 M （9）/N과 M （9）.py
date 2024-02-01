import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
elements = list(map(int, input().split()))


permutationsList = list(set(permutations(elements, M)))
permutationsList.sort()

for permutationPrint in permutationsList:
    if permutationPrint in permutationsList:
        print(' '.join(map(str, permutationPrint)))
