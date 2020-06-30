def negative(temperatures):
    days = 0
    for t in temperatures:
        if t < 0:
            days += 1
    return days

temperatures = [-1, 10, 13, -5, 8, -4]
print(negative(temperatures))
