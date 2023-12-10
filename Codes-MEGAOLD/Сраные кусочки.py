a = int(input())
b = int(input())
k = a

while k % a or k % b:
    k += a
print(k)
