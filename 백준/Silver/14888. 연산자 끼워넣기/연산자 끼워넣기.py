import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

operators = '+' * op[0] + '-' * op[1] + '*' * op[2] + '/' * op[3]
operator_perm = set(permutations(operators, N - 1))

max_result = -int(1e9)
min_result = int(1e9)

for ops in operator_perm:
    result = numbers[0]
    for i in range(1, N):
        if ops[i - 1] == '+':
            result += numbers[i]
        elif ops[i - 1] == '-':
            result -= numbers[i]
        elif ops[i - 1] == '*':
            result *= numbers[i]
        elif ops[i - 1] == '/':
            if result < 0:
                result = -(-result // numbers[i])
            else:
                result //= numbers[i]

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
