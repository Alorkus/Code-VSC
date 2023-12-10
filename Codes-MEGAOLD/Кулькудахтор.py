a = float(input())
b = float(input())
O = str(input())

if (O == "/" or O == "mod" or O == "div") and b == 0:
    c = "Деление на 0!"
elif O =="+": c = a + b
elif O =="-": c = a - b
elif O =="/": c = a / b
elif O =="*": c = a * b
elif O =="mod": c = a % b
elif O =="pow": c = a ** b
elif O =="div": c = a // b

print (c)
