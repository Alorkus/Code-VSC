def search4vowels(word):
    """Вывод гласных, что найдены в слове"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
