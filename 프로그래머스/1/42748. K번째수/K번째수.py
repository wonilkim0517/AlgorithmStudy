def solution(array, commands):
    answer = []

    # new_array = array[commands[0]:commands[1]]
    for command in commands:
        new_array = array[command[0] - 1 : command[1]]
        new_array.sort()
        answer.append(new_array[command[2] - 1])
        new_array = array
    return answer