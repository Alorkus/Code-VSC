v = int(input())
a = v//100
b = (v//10) % 10
c = v%10
s = a+b+c
p = a*b*c
print('Сумма цифр =', s)
print('Произведение цифр =', p)