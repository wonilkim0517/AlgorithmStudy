import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())
elements = list(map(int, input().split()))
elements.sort()

productList = list(product(elements, repeat=M))

for productPrint in productList:
    print(' '.join(map(str, productPrint)))