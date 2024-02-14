import sys
input=sys.stdin.readline

T=int(input())

def check(a):
    stack=[]
    for k in a:
        if k=='(':
            stack.append(k)
        elif k==')':
            if len(stack)==0:
                print("NO")
                return
            else:
                stack.pop()
                
    if len(stack)==0:
        print("YES")
        return
    else:
        print("NO")
        return

for i in range(T):
    b=list(input())
    check(b)