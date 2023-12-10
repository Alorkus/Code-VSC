n = input()
x = []
x += n
c = 0
x = sorted(x)
y = max(x)
if int(y)%3 == 0:
   c += 0
elif int(y)%3 != 0:
   x.remove(y)
   y = max(x)
if int(y)%3 == 0:
   print(y)
else:
   print('NO')

