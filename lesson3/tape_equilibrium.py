def solution(A):
    values = []
    for x in range(1, len(A)):
        difference = abs(sum(A[:x]) - sum(A[x:]))
        values.append(difference)
    
    return min(values)

A = [3, 1, 2, 4, 3]
print(solution(A))
