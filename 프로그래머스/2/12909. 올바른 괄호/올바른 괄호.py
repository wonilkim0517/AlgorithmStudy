def solution(s):
    stack = []
    
    for k in s:
        if k == '(':
            stack.append(k)
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False
    
    return True