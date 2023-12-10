work_mode = 'lock'
work_language = 'ru'
symbol = ['!','?','.',',','-',' ','>','<','"',')','(',':','*','@','#','№','$',';','%','^','&','+','/',chr(92)]
num_number = ['48','49','50','51','52','53','54','55','56','57']
work_step = 3

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
        elif text[i] in num_number:
            z = ord(text[i])
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

text = input()
encoder()
print(new_text)