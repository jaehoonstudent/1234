a = b = [1, 2, 3]
a[1] = 4
print(b)
b[0]=8
print(a)
a[2]=5
print(b)
print(id(a))
print(id(b))