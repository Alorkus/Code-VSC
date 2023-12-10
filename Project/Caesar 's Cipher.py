from random import *
from time import *

ru_low_number = ['1072','1073','1074','1075','1076','1077','1078','1079',
                '1080','1081','1082','1083','1084','1085','1086','1087','1088','1089',
                '1090','1091','1092','1093','1094','1095','1096','1097','1098','1099',
                '1100','1101','1102','1103']
ru_low_alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
#----------------------------------------------------------------------------------------------------------------------------------------------------
ru_up_number = ['1040','1041','1042','1043','1044','1045','1046','1047','1048','1049',
                '1050','1051','1052','1053','1054','1055','1056','1057','1058','1059',
                '1060','1061','1062','1063','1064','1065','1066','1067','1068','1069',
                '1070','1071']
ru_up_alphabet = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
#----------------------------------------------------------------------------------------------------------------------------------------------------
eng_low_number = ['97','98','99',
                '100','101','102','103','104','105','106','107','108','109',
                '110','111','112','113','114','115','116','117','118','119',
                '120','121','122']
eng_low_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#----------------------------------------------------------------------------------------------------------------------------------------------------
eng_up_number = ['65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90']
eng_up_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#----------------------------------------------------------------------------------------------------------------------------------------------------
num_number = ['48','49','50','51','52','53','54','55','56','57']
num = ['0','1','2','3','4','5','6','7','8','9']
#----------------------------------------------------------------------------------------------------------------------------------------------------
symbol = ['!','?','.',',','-',' ','>','<','"',')','(',':','*','@','#','№','$',';','%','^','&','+','/',chr(92)]

work_mode = ''
work_language = ''
work_step = 0
txt = ''
new_text = ''

print()
print('Enabling...')
print()
print('Вас приветствует бюджетная пародия на "Enigma"','Модуль способен работать в 2 режимах','В режиме шифровки - (зашифровка вашего текста)','И в режиме дешифровки - (рашифровка введенного текста)',sep='\n')
print()
print('Выберите режим работы и следуйте дальшейшим указаниям','Введите - "Ассанж" если хотете выбрать режим шифровки','Введите - "Тьюринг" если хотите выбрать режим дешифровки',sep='\n')
print()

def analysis(mode):
    global work_mode
    global work_language
    global txt
    if mode.isalpha():
        if mode.lower() == 'русский' and md == 2:
            work_language = 'ru'
            print('Выбранный язык ввода - Русский')
            print()
            return True
        if mode.lower() == 'english' and md == 2:
            work_language = 'eng'
            print('Выбранный язык ввода - Английский')
            print() 
            return True
        if mode.lower() == 'ассанж' and md == 1:
            print('Запуск в режиме шифрования')
            print()
            work_mode = 'lock'
            txt = 'Выберите шаг шифрования'
            return True
        elif mode.lower() == 'тьюринг' and md == 1:
            print('Запуск в режиме дешифровки')
            print()
            work_mode = 'unlock'
            txt = 'Вам известен шаг шифрования?'
            return True
        else:
            print('Ввод не распознан, повторите попытку')
            print()
            return False
    else:
        print('Ввод не распознан, повторите попытку')
        print()
        return False

def step_analysis():
    global work_step
    x = randint(1,15)
    y = randint(16,32)
    print(txt,'Введите его числом, например', x, 'или', y, ', или же введите "Нет"')
    print()
    step = input('Ввод: ')
    if step.isdigit():
        if int(step) == 0 or int(step) >= 33:
            print('Шаг не может быть меньше нуля, равняться ему или быть больше 32','Повторите ввод',sep='\n')
            return False
        else:
            work_step = int(step)
            print('Шаг задан -', step)
            print()
            return True
    elif step.lower() == 'нет':
        if work_mode == 'lock':
            print('При шифровке нужно выбрать шаг, повторите ввод согласно условиям')
            return False
        elif work_mode == 'unlock':
            print('Шаг неизвесетн, включен режим перебора')
            print()
            work_step = 0
            return True
    else:
        print('Ввод не распознан, пожалуйста, повторите ввод согласно условиям')
        print()
        return False

def text_analysis(text):
    cheker = 0
    numer = 0
    if text.isdigit():
        numer = 1
        print('Введенный текст содержит только цифры','Пожалуйста, повторите ввод согласно условиям',sep='\n')
        print()
        return False
    elif numer == 0:
        if work_language == 'eng':
            if cheker == 0:
                for i in range(len(text)):
                    if text[i] in ru_low_alphabet:
                        print('Текст содержит другой язык','Пожалуйста, повторите ввод согласно условиям',sep='\n')
                        print()
                        return False
                        break
                    else:
                        cheker = 1
            if cheker == 1:
                for i in range(len(text)):
                    if text[i] in ru_up_alphabet:
                        print('Текст содержит другой язык','Пожалуйста, повторите ввод согласно условиям',sep='\n')
                        print()
                        return False
                        break
                    else:
                        print('Другой язык не обнаружен','Текст одобрен',sep='\n')
                        print()
                        return True
        if work_language == 'ru':
            if cheker == 0:
                for i in range(len(text)):
                    if text[i] in eng_low_alphabet:
                        print('Текст содержит другой язык','Пожалуйста, повторите ввод согласно условиям',sep='\n')
                        print()
                        return False
                        break
                    else:
                        cheker = 1
            if cheker == 1:
                for i in range(len(text)):
                    if text[i] in eng_up_alphabet:
                        print('Текст содержит другой язык','Пожалуйста, повторите ввод согласно условиям',sep='\n')
                        print()
                        return False
                        break
                    else:
                        print('Другой язык не обнаружен','Текст одобрен',sep='\n')
                        print()
                        return True
    else:
        return False

def encoder():
    global new_text
    new_text = ''
    y1 = 0
    y2 = 0
    x5 = 48
    x6 = 57
    if work_language == 'ru':
        x1 = 1040
        x2 = 1071
        x3 = 1072
        x4 = 1103
    elif work_language == 'eng':
        x1 = 97
        x2 = 122
        x3 = 65
        x4 = 90
    for i in range(len(text)):
        if text[i] in symbol:
            new_text = new_text + text[i]
        elif text[i] in num:
            z = ord(text[i])
            z = z + work_step
            if z > x6:
                z = z - x6
                z = (x5+z)-1
                z = z + work_step
            elif x5 > z:
                z = x5-n
                z = (x6-z)+1
                z = z + work_step
            new_text = new_text + chr(z)
        else:
            n = ord(text[i])
            if x1 <= n <= x2:
                y1 = x1
                y2 = x2
                n = n + work_step
            elif x3 <= n <= x4:
                y1 = x3
                y2 = x4
                n = n + work_step
            if y1 <= n <= y2:
                new_text = new_text + chr(n)
            elif y1 > n:
                x = y1-n
                n = (y2-x)+1
                new_text = new_text + chr(n)
            elif n > y2:
                x = n-y2
                n = (y1+x)-1
                new_text = new_text + chr(n)
    return True
                
def decoder():
    global new_text
    new_text = ''
    y1 = 0
    y2 = 0
    x5 = 48
    x6 = 57
    if work_language == 'ru':
        x1 = 1040
        x2 = 1071
        x3 = 1072
        x4 = 1103
    elif work_language == 'eng':
        x1 = 97
        x2 = 122
        x3 = 65
        x4 = 90
    if work_step == 0:
        enumeration = 1
        while enumeration != 33:
            for i in range(len(text)):
                if text[i] in symbol:
                    new_text = new_text + text[i]
                elif text[i] in num:
                    z = ord(text[i])
                    z = z - enumeration
                    if z > x6:
                        z = z - x6
                        z = (x5+z)-1
                        z = z - enumeration
                    elif x5 > z:
                        z = x5-n
                        z = (x6-z)+1
                        z = z - enumeration
                    new_text = new_text + chr(z)
                else:
                    n = ord(text[i])
                    if x1 <= n <= x2:
                        y1 = x1
                        y2 = x2
                        n = n - enumeration
                    elif x3 <= n <= x4:
                        y1 = x3
                        y2 = x4
                        n = n - enumeration
                    if y1 <= n <= y2:
                        new_text = new_text + chr(n)
                    elif y1 > n:
                        x = y1-n
                        n = (y2-x)+1
                        new_text = new_text + chr(n)
                    elif n > y2:
                        x = n-y2
                        n = (y1+x)-1
                        new_text = new_text + chr(n)
            print()
            print('Вариент №', enumeration, new_text)
            sleep(0.7)
            enumeration += 1
            new_text = ''
    elif work_step != 0:
        enumeration = work_step
        for i in range(len(text)):
            if text[i] in symbol:
                new_text = new_text + text[i]
            elif text[i] in num:
                z = ord(text[i])
                z = z - enumeration
                if z > x6:
                    z = z - x6
                    z = (x5+z)-1
                    z = z - enumeration
                elif x5 > z:
                    z = x5-n
                    z = (x6-z)+1
                    z = z - enumeration
                new_text = new_text + chr(z)
            else:
                n = ord(text[i])
                if x1 <= n <= x2:
                    y1 = x1
                    y2 = x2
                    n = n - enumeration
                elif x3 <= n <= x4:
                    y1 = x3
                    y2 = x4
                    n = n - enumeration
                if y1 <= n <= y2:
                    new_text = new_text + chr(n)
                elif y1 > n:
                    x = y1-n
                    n = (y2-x)+1
                    new_text = new_text + chr(n)
                elif n > y2:
                    x = n-y2
                    n = (y1+x)-1
                    new_text = new_text + chr(n)
        print('Дешифровка завершена')
        print()
        print(new_text)
        print()
    else:
        print('404')
        return True


mode = input('Вводите: ')
md = 1
chek = analysis(mode)
while chek != True:
    mode = input('Вводите: ')
    chek = analysis(mode)

print('Выберите один из доступных языков','Для выбора русского языка, введите - "Русский"','Для выбора английского языка, введите - "English"',sep='\n')
print()

mode = input('Вводите: ')
md = 2
chek = analysis(mode)
while chek != True:
    mode = input('Вводите: ')
    chek = analysis(mode)

if work_mode == 'unlock':
    chek = step_analysis()
    while chek != True:
        chek = step_analysis()
elif work_mode == 'lock':
    chek = step_analysis()
    while chek != True:
        chek = step_analysis()

print('Запуск модуля...','Модуль запущен, действуйте согласно инструкциям на экране...',sep='\n')
print()

text_spiskom = input('Введите текст на выбранном Вами ранее языке: ').split()
text = ' '.join(text_spiskom)
chek = text_analysis(text)
while chek != True:
    text = input('Введите текст на выбранном Вами ранее языке: ')
    chek = text_analysis(text)

if chek == True and work_mode == 'lock':
    print('Шифрование.',' ',sep='\n')
    sleep(1)
    print('Шифрование..',' ',sep='\n')
    sleep(1)
    print('Шифрование...',' ',sep='\n')
    sleep(1)
    encoder()
    print('Шифрование завершено')
    print()
    print(new_text)
    print()
elif chek == True and work_mode == 'unlock':
    print('!!#^&^$%№ - Дешифровка.',' ',sep='\n')
    sleep(1)
    print('*/№^~&*#! - Дешифровка..',' ',sep='\n')
    sleep(1)
    print('!*!^/*//^ - Дешифровка...',' ',sep='\n')
    sleep(1)

    decoder()

print()
print('Работа модуля завершена')
print('3...')
sleep(0.6)
print('2...')
sleep(0.6)
print('1...')
sleep(0.6)
print('Выключение...',' ',sep='\n')    