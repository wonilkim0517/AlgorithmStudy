import sys
import math

input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


while True:
    n = int(input().strip())
    if n == 0:
        break

    count = 0

    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            count += 1

    print(count)