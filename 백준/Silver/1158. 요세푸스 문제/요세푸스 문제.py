from collections import deque
import sys
input=sys.stdin.readline

n, k = map(int,input().split())

stack=[]
q=deque()

for i in range(1,n+1):
    q.append(i)

while q:
    q.rotate(-(k-1))
    stack.append(q.popleft())
    
print(str(stack).replace('[','<').replace(']','>'))
    