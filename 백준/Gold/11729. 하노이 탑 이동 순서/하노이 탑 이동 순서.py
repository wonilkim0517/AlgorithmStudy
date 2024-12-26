import sys

input = sys.stdin.readline

N = int(input())
print(2**N-1)

def hanoi_tower(n, start, auxiliary, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n-1, start, end, auxiliary)
    print(start, end)
    hanoi_tower(n-1, auxiliary, start, end)

hanoi_tower(N, 1, 2,3)
