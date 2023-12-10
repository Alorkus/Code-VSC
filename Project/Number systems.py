print()
print('Включение...',' ','Запущен "Преобразователь систем счисления"',' ','Выберите исходную и конечную системы счисления',' ','Для выбора используйте русский язык и введите:','- Двоичная','- Восьмиричная','- Десятичная','- Шестнадцатеричная',sep='\n')
print()

Mode = 0
LogIn1 = 0
LogIn2 = 0
output_value = 0

def analysis():
    global Mode
    SisIn = input(word)
    if SisIn.isalpha():
        if SisIn.lower() == 'двоичная':
            Mode = 2
            return True
        elif SisIn.lower() == 'восьмиричная':
            Mode = 8
            return True
        elif SisIn.lower() == 'десятичная':
            Mode = 10
            return True
        elif SisIn.lower() == 'шестнадцатеричная':
            Mode = 16
            return True
    else:
        print('Несоответствующий ввод, повторите попытку согласно заданным условиям')
        print()
        return False

def converter():
    global output_value
    if LogIn1 == 2:
        x = str(Num)
        y = int(x,2)
        if LogIn2 == 8:
            z = oct(y)
            output_value = z[2:]
        elif LogIn2 == 10:
            output_value = y
        elif LogIn2 == 16:
            z = hex(y)
            output_value = x[2:]
    elif LogIn1 == 8:
        x = str(Num)
        y = int(x,8)
        if LogIn2 == 2:
            z = bin(y)
            output_value = z[2:]
        elif LogIn2 == 10:
            output_value = y
        elif LogIn2 == 16:
            z = hex(y)
            output_value = x[2:]
    elif LogIn1 == 10:
        x = str(Num)
        y = int(x,10)
        if LogIn2 == 2:
            z = bin(y)
            output_value = z[2:]
        elif LogIn2 == 8:
            z = oct(y)
            output_value = z[2:]
        elif LogIn2 == 16:
            z = hex(y)
            output_value = x[2:]
    elif LogIn1 == 16:
        x = str(Num)
        y = int(x,16)
        if LogIn2 == 2:
            z = bin(y)
            output_value = z[2:]
        elif LogIn2 == 8:
            z = oct(y)
            output_value = z[2:]
        elif LogIn2 == 10:
            output_value = y
    print()
    print(output_value)
    print()
    return True

word = 'Выберите исходную систему : '
chek = analysis()
while chek != True:
    chek = analysis()
LogIn1 = Mode

print()

word = 'Выберите конечную систему : '
chek = analysis()
while chek != True:
    chek = analysis()
LogIn2 = Mode

print()
Num = input('Системы заданы, теперь введите число: ')
converter()
print('Преобразование завершено',' ',sep='\n')