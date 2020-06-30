"""
a = False
b = False
c = a ^ b = False

a = True
b = True
c = a ^ b = False

a = True
b = False
c = a ^ b = True

a = False
b = True
c = a ^ b = True
"""
# lista = [1, 1, 2, 3, 3, 3, 3, 1, 1]
# result = 0

# for i in lista:
#     result = result ^ i

# print(result)
a = 1
b = 0
a, b = b, a

print(a, b)

a = 11
b = 11
c = 2
d = 3
e = 3
f = 100
g = 2
print("a ^ b", a ^ b ^ c ^ d ^ e ^ f ^ g)
