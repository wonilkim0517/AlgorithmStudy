def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        # i번째부터 j번째까지 짜른 배열 추출
        new_array = array[i - 1 : j]
        # 배열 정렬
        new_array.sort()
        # 배열의 k번째 값을 answer에 저장
        answer.append(new_array[k - 1])
        # 배열 초기화
        new_array = array
    return answer