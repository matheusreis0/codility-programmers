def linear(n, A):
    for i in range(n):
        if A[i] == 0:
            return 0
    
    return 1


def linear2(n, m):
    result = 0

    for i in range(n):
        result += i
    for j in range(m):
        result += j
    
    return result


print(linear(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(linear2(10, 20))
