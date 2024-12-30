def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 도난당한 경우를 먼저 제거
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    
    # 빌려줄 수 있는지 확인
    for i in lost_only[:]:
        if i - 1 in reserve_only:
            lost_only.remove(i)
            reserve_only.remove(i - 1)
        elif i + 1 in reserve_only:
            lost_only.remove(i)
            reserve_only.remove(i + 1)
            
    #수업을 들을 수 있는 학생의 수
    answer = n - len(lost_only)
    return answer