a = int(input())
b = int(input())
c = int(input())

A = []

A.append(a)
A.append(b)
A.append(c)

B = (sorted(A))
a1 = B.pop(2)
b1 = B.pop(0)
c1 = B.pop(0)

print(a1)
print(b1)
print(c1)

