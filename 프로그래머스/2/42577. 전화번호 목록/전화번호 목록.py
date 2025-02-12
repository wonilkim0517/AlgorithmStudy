def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        k = phone_book[i]
        if phone_book[i + 1][:len(k)] == k:
            return False
        
    return True