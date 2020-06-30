def quadratic(n):
    result = 0

    for i in range(n):
        for j in range(i, n):
            result += 1
    
    return result

print(quadratic(10))
