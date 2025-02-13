def solution(numbers):
    answer = 0
    numbers_str = list(map(str, numbers))
    
    numbers_str.sort(key = lambda x: str(x) * 3, reverse=True)
    answer = ''.join(map(str, numbers_str))
    
    if answer[0] == '0':
        return '0'
    
    return answer