import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())
elements = list(map(int, input().split()))
elements.sort()

productList = list(product(elements, repeat=M))
productList.sort()
visited = set()

for productPrint in productList:
    productPrint_current = tuple(productPrint)
    if productPrint_current not in visited:
        visited.add(productPrint_current)
        print(' '.join(map(str, productPrint)))
