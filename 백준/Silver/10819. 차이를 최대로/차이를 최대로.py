import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
permutationsList = list(permutations(A))
answerList = []

for permutationsPrint in permutationsList:
    answer = 0
    for i in range(N - 1):
        answer += abs(permutationsPrint[i] - permutationsPrint[i + 1])
    answerList.append(answer)
print(max(answerList))
