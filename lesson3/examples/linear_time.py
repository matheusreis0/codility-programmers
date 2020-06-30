def linear(n, A):
    for i in range(n):
        if A[i] == 0:
            return 0
    
    return 1

print(linear(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
