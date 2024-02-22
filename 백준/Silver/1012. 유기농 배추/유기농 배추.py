import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(x, y):
    if (x < 0 or x > N - 1) or (y < 0 or y > M - 1):
        return False

    if farm[x][y] == 1:
        farm[x][y] = 0

        # 인접한 좌표 조사
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    cnt = 0

    for x in range(N):
        for y in range(M):
            if dfs(x, y):
                cnt += 1

    print(cnt)
