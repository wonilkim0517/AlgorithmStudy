import sys

input = sys.stdin.readline

N = int(input())

progression = []
result = 0

for _ in range(N):
    n = int(input())
    progression.append(n)

positives = []
negatives = []
ones = 0

for i in progression:
    if i > 1:
        positives.append(i)
    elif i < 0:
        negatives.append(i)
    elif i == 1:
        ones += 1

positives.sort(reverse=True)
negatives.sort()

while len(positives) > 1:
    max_1 = positives.pop(0)
    max_2 = positives.pop(0)
    result += max_1 * max_2

if positives:
    result += positives[0]

while len(negatives) > 1:
    min_1 = negatives.pop(0)
    min_2 = negatives.pop(0)
    result += min_1 * min_2

if negatives:
    if 0 in progression:
        result += 0
    else:
        result += negatives[0]

result += ones
print(result)
