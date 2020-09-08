"""
n = int(input())
v1 = list(map(int, input()))
v2 = list(map(int, input()))
soma = [0] * n

for i in range(n):
    soma[i] = v1[i] + v2[i]

for item in soma:
    print(item)
"""

def sum_lists(v1: list, v2: list):
    if (len(v1) != len(v2)):
        return
    n = len(v1)
    soma = [0] * n

    for i in range(n):
        soma[i] = v1[i] + v2[i]

    print([item for item in soma])

v1 = list(map(int, input()))
v2 = list(map(int, input()))
sum_lists(v1, v2)
