def solution(N):
    num = bin(n)

    binary_gap = 0
    previous_gap = 0

    for i in range(2, len(num)):
        if num[i] == '0':
                binary_gap += 1
        else:
            if binary_gap > previous_gap:
                previous_gap = binary_gap
            binary_gap = 0
    
    return previous_gap

n = 1041

"""
binary_number_list = []
    binary_gap = 0
    previous_gap = 0

    while N > 0:
        resto = N % 2
        N = N // 2
        binary_number_list.append(resto)

    for value in binary_number_list[::-1]:
        if value == 0:
            binary_gap += 1
        else:
            if binary_gap > previous_gap:
                previous_gap = binary_gap
            binary_gap = 0

    return previous_gap
"""

print(solution(n))
