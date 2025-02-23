from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    order = 0
    
    while q:
        n = q.popleft()
        
        if any(n[1] < item[1] for item in q):
            q.append(n)
        else:
            order += 1
            if n[0] == location:
                return order
        