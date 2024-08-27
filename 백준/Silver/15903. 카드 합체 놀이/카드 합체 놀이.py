import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for _ in range(m):
    min_1 = min(cards)
    cards.remove(min_1)

    min_2 = min(cards)
    cards.remove(min_2)

    sum_min = min_1 + min_2

    cards.extend([sum_min, sum_min])

result = sum(cards)

print(result)
