from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    numList = list(map(int, input().split()))
    if numList == [0]:
        break

    lottoList = combinations(numList[1:], 6)

    for lottoPrint in lottoList:
        print(*lottoPrint)
    print()