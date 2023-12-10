from random import *

set_of_Low_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
set_of_Up_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
set_of_numbers = ['0','1','2','3','4','5','6','7','8','9']
set_of_symbol = ['!','#','$','%','&','*','+','-','=','?','@','^','_']
set_of_ambiguous = ['i','l','1','L','o','0','O']
valid_set = []
x = ''
num = 0

print()
print('Enabling...')
print()
print('Приветствую вас, в модуле "Генерация паролей"')
print('Модуль может сгенерировать пароль, по заданным вами параметрам','Вы сами можете выбрать размер,состав и вид пароля',sep='\n')
print('Для запуска модуля напишите "Старт"','Любой другой ввод завершит работу',sep='\n')
print()

def number(approve_num):
    if approve_num.isdigit():
        if num <= int(approve_num):
            return True
        else:
            print('Введенное число, выходит за допустимые пределы, попробуйте снова')
            return False
    else:
        print('Вы ввели не число, пожалуйста, введите число')
        return False

def approved(approve):
    if approve.isalpha():
        if approve.lower() == 'да':
            print('Символы', x, 'разрешены...')
            return True
        elif approve.lower() == 'нет':
            print('Символы', x, 'запрещены...')
            return True
        else:
            print('Ввод не распознан, пожалуйста, введите "Да" или "Нет"')
            return False
    else:
        print('Ввод не распознан, пожалуйста, введите "Да" или "Нет"')
        return False

def pass_properties(entry):
    if entry.lower() == 'старт':
        print('Запуск модуля...','Пожалуйста, следуйте инструкциям на экране...', sep='\n')
        print('Задайте количество генерируемых паролей, напишите любой целое число больше 0')
        print()
        global num
        num = 1
        a_quantity = input()
        approve_num = a_quantity
        chekA = number(approve_num)
        while chekA != True:
            a_quantity = input()
            approve_num = a_quantity
            chekA = number(approve_num)
        if chekA == True:
            A = int(a_quantity)
        print()

        print('Задайте длину вашего пароля, напишите любой целое число больше 4')
        print()
        num = 4
        b_length = input()
        approve_num = b_length
        chekB = number(approve_num)
        while chekB != True:
            b_length = input()
            approve_num = b_length
            chekB = number(approve_num)
        if chekB == True:
            B = int(b_length)
        print()

        print('Включать ли символы "0123456789"', 'Введите "Да" или "Нет"',sep='\n')
        print()
        global x
        x = '"0123456789"'
        c_approve = input()
        approve = c_approve
        chekC = approved(approve)
        while chekC != True:
            c_approve = input()
            approve = c_approve
            chekC = approved(approve)
        if chekC == True:
            C = c_approve.lower()
        print()

        print('Включать ли символы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"', 'Введите "Да" или "Нет"',sep='\n')
        print()
        x = '"ABCDEFGHIJKLMNOPQRSTUVWXYZ"'
        d_approve = input()
        approve = d_approve
        chekD = approved(approve)
        while chekD != True:
            d_approve = input()
            approve = d_approve
            chekD = approved(approve)
        if chekD == True:
            D = d_approve.lower()
        print()

        print('Включать ли символы "abcdefghijklmnopqrstuvwxyz"', 'Введите "Да" или "Нет"',sep='\n')
        print()
        x = '"abcdefghijklmnopqrstuvwxyz"'
        e_approve = input()
        approve = e_approve
        chekE = approved(approve)
        while chekE != True:
            e_approve = input()
            approve = e_approve
            chekE = approved(approve)
        if chekE == True:
            E = e_approve.lower()
        print()

        print('Включать ли символы "!#$%&*+-=?@^_"', 'Введите "Да" или "Нет"',sep='\n')
        print()
        x = '"!#$%&*+-=?@^_"'
        f_approve = input()
        approve = f_approve
        chekF = approved(approve)
        while chekF != True:
            f_approve = input()
            approve = f_approve
            chekF = approved(approve)
        if chekF == True:
            F = f_approve.lower()
        print()

        print('Разрешить ли использование неоднозначных символов "il1Lo0O"', 'Введите "Да" или "Нет"',sep='\n')
        print()
        x = '"il1Lo0O"'
        g_approve = input()
        approve = g_approve
        chekG = approved(approve)
        while chekG != True:
            g_approve = input()
            approve = g_approve
            chekG = approved(g_approve)
        if chekG == True:
            G = g_approve.lower()
        print()
        return A,B,C,D,E,F,G

def pass_generation():
    quantity = int(A)
    length = int(B)
    answer = []
    count = 0
    while quantity != 0:
        quantity -= 1
        count += 1
        answer = []
        for i in range(length):
            y = randint(0, len(valid_set)-1)
            enter = valid_set[y]
            answer.extend(enter)
        print('Пароль №', count)
        print(*answer,sep='')
        print()
    print('Все пароли для вас сгенерированны','Спасибо, что воспользовались модулем генерации, будем рады видеть вас снова','Досвидания!','Shutting down...',sep='\n')
    print()



entry = input()
if entry.lower() == 'старт':
    count = 1
    A,B,C,D,E,F,G = pass_properties(entry)
    if C == 'нет' and D == 'нет' and E == 'нет' and F == 'нет' and G == 'нет':
        count = 0
        print('Вы запретили все предложенные наборы символов...','Генерация паро(ля/лей) невозможна...',sep='\n')
    if C == 'да':
        valid_set.extend(set_of_numbers)
    if D == 'да':
        valid_set.extend(set_of_Up_letters)
    if E == 'да':
        valid_set.extend(set_of_Low_letters)
    if F == 'да':
        valid_set.extend(set_of_symbol)
    if G == 'нет':
        if 'i' in valid_set:
            valid_set.remove('i')
        if 'l' in valid_set:
            valid_set.remove('l')
        if '1' in valid_set:
            valid_set.remove('1')
        if 'L' in valid_set:
            valid_set.remove('L')
        if 'o' in valid_set:
            valid_set.remove('o')
        if 'O' in valid_set:
            valid_set.remove('O')
        if '0' in valid_set:
            valid_set.remove('0')
    if count != 0:
        print('Условия заданы и сохранены','Генерация паро(ля/лей)...',sep='\n')
        pass_generation()
else:
    print()
    print('Shutting down...')
    print()