def solution(nums):
    # 폰켓몬 종류 수
    nums_count = len(set(nums))
    
    # 최대로 고를 수 있는 수 (배열의 길이 / 2)
    max_selectable_count = len(nums) / 2
    
    
    answer = min(nums_count, max_selectable_count)
    return answer