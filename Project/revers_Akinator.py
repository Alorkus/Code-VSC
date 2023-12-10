from random import *

x = 0
y = 100
start = 0

print()
print('Enabling...')
print()
print('Вас приветствует обратная версия "Числовой угадайки"','Основным отличием данной версии, является то, что число здесь, загадываете вы, а модуль будет угадывать',sep='\n')
print()
print('Желаете сыграть?','Введите "Да" или "Старт" для начала игры','Любой другой ввод, завершит работу модуля',sep='\n')
print()

def validate(play_or_not):
    global start
    if play_or_not.isalpha():
        if play_or_not.lower() == 'да' or play_or_not.lower() == 'старт':
            print()
            print('Отличный выбор! Мы начинаем')
            print()
            start = 1
            return True
        else:
            print()
            print('Очень жаль, возвращайтесь если передумаете')
            print('Shutting down...')
            print()
            return True
    else:
        print('Ввод не распознан, попробуйте ещё раз')
        print()
        return False

def valid_num(n):
    if n.isdigit():
        if int(n) > y:
            print('Граница выше допустимой...','Повторите ввод',sep='\n')
            print()
            return False
        else:
            return True
    else:
        print('Введено не число, повторите ввод')
        print()
        return False

def borders(the_borders):
    global x
    global y
    y = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    if the_borders.isalpha():
        if the_borders.lower() == 'да':
            print()
            print('Запрошена смена границ')
            n = input('Выберите правую ганицу ')
            cheker = valid_num(n)
            while cheker != True:
                n = input('Выберите правую ганицу ')
                cheker = valid_num(n)
            y = int(n)
            print('Правая граница изменена -', y)
            print()
            n = input('Выберите левую ганицу ' )
            cheker = valid_num(n)
            while cheker != True:
                n = input('Выберите правую ганицу ' )
                cheker = valid_num(n)
            x = int(n)
            print('Левая граница изменена -', x)
            print()
            print('Новые границы назначены','Левая - ',x,'Правая -',y)
            print('Убедительная просьба, НЕ выходить за эти границы при загадывании числа')
            print()
            return True
        elif the_borders.lower() == 'нет':
            y = 100
            print('Границы в заводских настройках')
            print()
            return True
        else:
            print('Ввод не распознан','Повторите ввод...',sep='\n')
            print()
            return False

def valid(ans):
    global Left
    global Right
    if ans.isalpha():
        if ans.lower() == 'да':
            return True
        elif ans.lower() == 'больше':
            Left = (int(possible))+1
            return True
        elif ans.lower() == 'меньше':
            Right = (int(possible))-1
            return True
        else:
            return False
    else:
        return False


def game():
    global possible
    global count
    possible = randint(Left,Right)
    count += 1
    print('Ваше число - ',possible,'?')
    print()
    ans = input('Введите "Да" или укажите, что ваше число "больше" или же "меньше" указанного - ' )
    print()
    chek = valid(ans)
    while chek != True:
        ans = input('Введите ответ на вопрос согласно правилам -')
        chek = valid(ans)
    if ans.lower() == 'да':
        return True
    else:
        return False



play_or_not = input()
chek = validate(play_or_not)
while chek != True:
    play_or_not = input()
    chek = validate(play_or_not)

if start == 1:
    print('Заводские границы работы модуля имеют вид [0:100], но эти границы динамичны, вы сможете их изменить по желанию','Желаете сменить границы?',sep='\n')
    print()
    print('Введите "Да" или "Нет"')
    print()
    the_borders = input()
    chek = borders(the_borders)
    while chek != True:
        the_borders = input()
        chek = borders(the_borders)

if start == 1:
    print('Загадайте любое число в заданных вами грацницах, мы начинаем','3...','2...','1...',sep='\n')
    print()
    Left = int(x)
    Right = int(y)
    count = 0
    game()
    answer = game()
    while answer != True:
        game()
        answer = game()
    print()
    print('Число угадано ву-хуу!')
    print('Число попыток =', count)
    print()