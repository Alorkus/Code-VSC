a = int(input())
b = int(input())
a1 = (a/b)
b1 = (b/a)
n = 0.1

if ((a // b == a1) or (a // b == b1)) or ((b // a == a1) or (b // a == b1)):
    if a>b:
        print(a)
    else:
        print(b)
elif a != b:
    if n//a != n//b:
        n += 1
    else:
        print (n)
else:
    print(a)
