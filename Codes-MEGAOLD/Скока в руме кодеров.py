A = int(input())

if ((A % 10 == 1) and (A % 100 != 11)):
    print(A, 'программист')
elif (A % 10 in (2,3,4) or A % 100 in (2,3,4)) and not A % 100 in (12,13,14):
    print(A, 'программиста')
else:
    print(A, 'программистов')
