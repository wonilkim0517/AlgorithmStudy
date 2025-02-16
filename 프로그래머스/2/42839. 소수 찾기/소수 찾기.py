from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    numberSet = set()
    numbers_int = list(map(int, numbers))
    
    for i in range(1, len(numbers_int) + 1):
        for perm in permutations(numbers, i):
            num = int("".join(perm))
            a = set(permutations(numbers_int, i))
            numberSet.add(num)
    
    for k in numberSet:
        if is_prime(k):
            answer += 1
    
    return answer