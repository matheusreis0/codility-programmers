def solution(A):
    A.sort()
    size = len(A)

    for i in range(size):
        value = i + 1
        if value != A[i]:
            return value

    return size + 1

"""
def solution(A):
    array = A
    array.sort()

    for i in range(len(array)):
        num = i + 1
        if array[i] == num:
            pass
        else:
            return num
    
    return 1
"""

array = [1, 2, 3, 5]
array = []

print(solution([array]))
