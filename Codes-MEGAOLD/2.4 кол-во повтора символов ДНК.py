s = str(input())
s1 = s + '1'
a = ''
b = s[0]
c = 0
c1 = ''

for i in s1:
    if b == i:
        c += 1
    else:
        c1 = str(c)
        a += b
        a = a + c1
        c = 1
        c1 = ''
        b = i
print(a)
