import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        mix_scoville = first + (second * 2)
        heapq.heappush(scoville, mix_scoville)
        answer += 1
    return answer