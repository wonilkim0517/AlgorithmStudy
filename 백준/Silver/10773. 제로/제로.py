import sys

input = sys.stdin.readline

K = int(input())

result = 0
ledger = []
for _ in range(K):
    n = int(input())

    if n == 0:
        ledger.pop()
    else:
        ledger.append(n)

result = sum(ledger)
print(result)
