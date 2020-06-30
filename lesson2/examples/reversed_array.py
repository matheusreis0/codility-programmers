def reverse(A):
    N = len(A)
    for i in range(N // 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A

list_example = ['a', 'b', 'c']
print(reverse(list_example))
