def solution(number):
    if number == 1:
        return 1
    else:
        return number * solution(number - 1)


print(solution(5))