import sys

n=int(sys.stdin.readline())

for _ in range(n):
    t, w = sys.stdin.readline().split()
    t= int(t)
    w= str(w)
    for i in range(len(w)):
        print(t*w[i], end='')
    print()