# def solution(A):
#     values = []
#     for x in range(1, len(A)):
#         difference = abs(sum(A[:x]) - sum(A[x:]))
#         print(difference)
#         values.append(difference)
    
#     return min(values)

# def solution(A):
#     chop_1 = A[0]
#     chop_2 = sum(A[1:])
#     min_diff = abs(chop_1 - chop_2)
#     for i in range(1, len(A) - 1):
#         chop_1 += A[i]
#         chop_2 -= A[i]
#         if abs(chop_1 - chop_2) < min_diff:
#             min_diff = abs(chop_1 - chop_2)

#     return min_diff

def solution(A):
    left, right = 0, sum(A)
    best = float('Inf')
    for a in A[:-1]:
        left += a
        right -= a
        best = min(best, abs(left - right))

    return best

# A = [3, 1, 2, 4, 3]
A = [-1000, 1000]
print(solution(A))
