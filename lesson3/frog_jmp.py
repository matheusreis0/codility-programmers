def solution(X, Y, D):
    jumps = 0

    diff = Y - X

    if diff % D == 0:
        jumps = diff // D
    else:
        jumps = diff // D + 1

    return jumps


x = 10
y = 85
d = 30

print(solution(x, y, d))
