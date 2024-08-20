import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
answer = 0

for _ in range(N):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)

for i in coins:
    answer += K // i
    K %= i

print(answer)