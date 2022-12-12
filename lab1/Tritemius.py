

ALPHABET_ENG = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def tritemiusLinear(alphabet, plainText, valueA, valueB):
    cryptoText = ''
    letter_position = 0
    for letter in plainText.lower():
        if letter in alphabet:
            valueK = (valueA * letter_position +valueB) % len(alphabet)
            valueY = (alphabet.find(letter) + valueK) % len(alphabet)
            cryptoText += alphabet[valueY]
            # letter_position += 1
        else:
            cryptoText += letter
        letter_position += 1
    print(cryptoText)
    return cryptoText

def tritemiusSquare(alphabet, plainText, valueA, valueB, valueC):
    cryptoText = ''
    letter_position = 0
    for letter in plainText.lower():
        if letter in alphabet:
            valueK = (valueA * letter_position * letter_position + valueB * letter_position + valueC) % len(alphabet)
            valueY = (alphabet.find(letter) + valueK) % len(alphabet)
            cryptoText += alphabet[valueY]
            # letter_position += 1
        else:
            cryptoText += letter
        letter_position += 1
    print(cryptoText)
    return cryptoText

def deTritemiusLinear(alphabet, cryptoText):
    plainText = ''
    letter_position = 0
    for valueA in range(1, 6):
        for valueB in range(1, 6):
                for letter in cryptoText.lower():
                    if letter in alphabet:
                        valueK = (valueA * letter_position + valueB) % len(alphabet)
                        valueX = (alphabet.find(letter) -
                                  valueK) % len(alphabet)
                        plainText += alphabet[valueX]
                    else:
                        plainText += letter
                    letter_position += 1
                print(f'A = {valueA}, B = {valueB}')
                print(plainText)
                letter_position = 0
                plainText = ''

def deTritemiusSquare(alphabet, cryptoText):
    plainText = ''
    letter_position = 0
    for valueA in range(1,6):
        for valueB in range(1,6):
            for valueC in range(1,6):
                for letter in cryptoText.lower():
                    if letter in alphabet:
                        valueK = (valueA * letter_position * letter_position + valueB * letter_position + valueC) % len(alphabet)
                        valueX = (alphabet.find(letter) - valueK) % len(alphabet)
                        plainText += alphabet[valueX]
                    else:
                        plainText += letter
                    letter_position += 1
                print(f'A = {valueA}, B = {valueB}, C = {valueC}')
                print(plainText)
                letter_position = 0
                plainText = ''


    
# tritemiusSquare(ALPHABET_ENG, "Ende gut, alles gut", 1, 3, 2)
# tritemiusLinear(ALPHABET_ENG, "Aller Anfang ist schwer", 2, 3)
# tritemiusLinear(ALPHABET_ENG, "AND IT IS LIFE", 1, 2)
deTritemiusSquare(ALPHABET_ENG, "FDXZZRGMAG KZI IVB UDATMMC QL SCZP")
# deTritemiusSquare(ALPHABET_ENG, "gtpy wyn, cllgy ayj")
# deTritemiusLinear(ALPHABET_ENG, "ZOWJ UGSC")