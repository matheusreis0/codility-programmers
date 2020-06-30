def slow_solution(n):
    result = 0

    for i in range(n):
        for j in range(i + 1):
            result += 1

    return result

def fast_solution(n):
    result = 0

    for i in range(n):
        result += (i + 1)

    return result

def model_solution(n):
    result = n * (n + 1) // 2
    return result

print(model_solution(4))
