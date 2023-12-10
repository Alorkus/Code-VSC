V = str(input())
T = 'треугольник'
P = 'прямоугольник'
K = 'круг'
Pi = 3.14
if V == T:
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a+b+c)/2)
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print(S)
elif V == P:
    a = int(input())
    b = int(input())
    S = (a*b)
    print(S)
else:
    a = int(input())
    S = (Pi*(a*a))
    print(S)
