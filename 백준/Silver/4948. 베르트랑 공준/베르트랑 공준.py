import sys
import math

input = sys.stdin.readline

def sieve(max_limit):
    """ 에라토스테네스의 체를 사용해 소수 테이블 생성 """
    is_prime = [True] * (max_limit + 1)
    is_prime[0], is_prime[1] = False, False # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(max_limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_limit + 1, i):
                is_prime[j] = False
    return is_prime

# 최대 범위 설정 및 소수 테이블 생성
MAX_LIMIT = 123456 * 2  # 최대 n 범위
prime_table = sieve(MAX_LIMIT)

while True:
    n = int(input().strip())
    if n == 0:
        break

    # n+1부터 2n까지의 소수 개수 계산
    count = sum(prime_table[n + 1: 2 * n + 1])
    print(count)
