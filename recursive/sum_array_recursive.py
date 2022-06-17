def solution(numbers: list) -> int:
    if numbers == []:
        return 0
    else:
        return numbers[0] + solution(numbers[1::])


print(solution([2,4,6]))
