import heapq

def solution(scoville, K):
    answer = 0
    
    # 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    
    # 첫 번째 값이 K 다 클 때 까지
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        # 가장 작은 두 값 추출
        fisrt = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 섞은 음식의 스코빌 지수
        mix_scoville = fisrt + (second * 2)
        heapq.heappush(scoville, mix_scoville)
        answer += 1
    return answer