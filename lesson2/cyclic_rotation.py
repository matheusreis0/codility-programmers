def solution(A, K):
    if len(A) > 0:
        for i in range(K):
            last_index = len(A) - 1
            last_item = A[last_index]
            A.pop(last_index)
            A.insert(0, last_item)

    return A

"""
    last_index = len(A) - 1
    new_array = [0] * len(A)

    for i in range(K):
        for index, value in enumerate(A):
            if index != last_index:
                new_array[index + 1] = value
            else:
                new_array[0] = value
                A = []
                A += new_array
    else:
        new_array = A

    return new_array
"""

array = []
times = 1

print(solution(array, times))

print(array)

