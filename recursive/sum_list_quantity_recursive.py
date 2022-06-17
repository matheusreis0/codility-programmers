def solution(numbers: list) -> int:
    if numbers == []:
        return 0
    else:
        return 1 + solution(numbers[1::])


print(solution([1,2,3]))
