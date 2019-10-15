table_number = {
    'một' : 1,
    'hai' : 2,
    'ba'  : 3,
    'bốn' : 4,
    'năm' : 5,
    'sáu' : 6,
    'bảy' : 7,
    'tám' : 8,
    'chín' : 9
}

def convert1Digit(text):
    if text == 'mười':
        return 10
    return table_number.get(text)

def convert2Digit(words):
    len_of_words = len(words)
    chuc, donvi = None, None

    if (len_of_words == 2) or (words[1] == 'mươi' and len_of_words == 3):
        chuc = None if words[0] == 1 else table_number.get(words[0])
        donvi = table_number.get(words[-1])
    
    if len_of_words == 2:
        if words[1] == 'mươi':
            chuc = table_number.get(words[0])
            donvi = 0
        if words[0] == 'mười':
            chuc = 1
            donvi = table_number.get(words[1])

    if chuc != None and donvi != None:
        return 10 * chuc + donvi


def convert3Digit(words):
    len_of_words = len(words)
    hangTram = table_number.get(words[0])
    
    if len_of_words == 2:
        return hangTram * 100

    if len_of_words == 3 and words[1] == 'mười':
        return hangTram * 100 + 10
    
    if len_of_words == 4 and words[2] in ['lẻ', 'linh']:
        donvi = 4 if words[3] == 'tu' else table_number.get(words[3])
        if donvi != None:
            return 100 * hangTram + donvi

    value2digit = convert2Digit(words[2:])
    if value2digit != None:
        return 100 * hangTram + value2digit


while True:
    text = input('text = ')
    words = text.strip().split()

    if len(words) == 1:
        print(convert1Digit(text))
    elif words[0] in table_number and words[1] == 'trăm':
        print(convert3Digit(words))
    else:
        print(convert2Digit(words))