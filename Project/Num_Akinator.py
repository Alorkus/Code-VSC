from random import *
print()
print('Добро пожаловать в "Числовую Угадайку"')
print('Пожалуйста, введите целое число от 1 до 100')
print()

def accepted(text):
    if text.isdigit():
        if 1 <= int(text) <= 100:
            return True
        else:
            print('Введенное число, выходит за допустимые пределы, попробуйте снова')
            print()
            return False
    else:
        print('Вы ввели не число, пожалуйста, введите число')
        print()
        return False

def akinator(text):
    num = randint(1,100)
    count = 0
    chek = True
    while text != num:
        if chek != True:
            text = input()
            chek = accepted(text)
        elif int(text) < num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще раз')
            print()
            text = input()
            chek = accepted(text)
        elif int(text) > num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще раз')
            print()
            text = input()
            chek = accepted(text)
        elif int(text) == num:
            print('Вы угадали, правильное число', text, 'поздравляем!')
            print('Количество попыток :', count)
            print()
            print('У вас отлично получается, давайте сыграем еще разок?','Напиши "Да", если согласны или же "что-то другое" в случае отказа.',sep='\n')
            print()
            new_game = input()
            print()
            if new_game.lower() == 'да':
                print('Играем!')
                print()
                text = input('Ввод: ')
                chek = accepted(text)
                while chek != True:
                    text = input('Ввод: ')
                    chek = accepted(text)
                if chek == True:
                    akinator(text)
            break

text = input('Ввод: ')
chek = accepted(text)
while chek != True:
    text = input('Ввод: ')
    chek = accepted(text)

if chek == True:
    akinator(text)

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print()