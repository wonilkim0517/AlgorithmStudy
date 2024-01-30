import sys
from itertools import product

N, M = map(int, input().split())

elements = [i + 1 for i in range(N)]
productList = list(product(elements, repeat=M))

for productPrint in productList:
    print(' '.join(map(str, productPrint)))