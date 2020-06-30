array = []
times = 15

def solution(A, K):
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

print(solution(array, times))
