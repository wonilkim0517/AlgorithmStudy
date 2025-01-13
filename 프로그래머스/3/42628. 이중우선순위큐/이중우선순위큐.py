import heapq

def solution(operations):
    answer = []
    lists = []
    
    for k in operations:
        operator = k[0] # 연산자
        value = int(k[2:]) # 값

        # 연산자가 I면 heappush
        if operator == 'I':
            heapq.heappush(lists, value)
        
        # 연산자가 D이고
        if lists and operator == 'D':
            # 값이 1이면 최댓값 제거
            if value == 1:
                lists = heapq.nlargest(len(lists), lists)[1:]
                heapq.heapify(lists)
            # 값이 -1이면 최솟값 제거
            elif value == -1:
                lists = heapq.nsmallest(len(lists), lists)[1:]
                # heapq.heapify(lists)
        
    if lists:
        # 최댓값 최솟 값 answer에 append
        answer.append(heapq.nlargest(len(lists), lists)[0])
        answer.append(heapq.nsmallest(len(lists), lists)[0])
    else:
        answer.append(0)
        answer.append(0)
    return answer