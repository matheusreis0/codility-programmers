def solution(numbers: list) -> int:
    if len(numbers) == 2:
        return numbers[0] if numbers[0] > numbers[1] else numbers[1]
    highest = solution(numbers[1::])
    return numbers[0] if numbers[0] > highest else highest 


print(solution([1,2,3]))
