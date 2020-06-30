def solution(X, Y, D):
    jumps = 0

    while X < Y:
        jumps += 1
        X += D

    return jumps


x = 1
y = 5
d = 2

print(solution(x, y, d))
