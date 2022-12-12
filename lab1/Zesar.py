

alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def zesar(alphabet, plainText, step):
    cryptoText = ''
    for letter in plainText.lower():
        if letter in alphabet:
            cryptoText += alphabet[((alphabet.find(letter)) + step) % len(alphabet)]
        else:
            cryptoText += letter
    print(cryptoText)
    return cryptoText

def deZesar(alphabet, cryptoText):
    step = len(alphabet)
    while step != 0:
        plainText = ''
        for letter in cryptoText.lower():
                if letter in alphabet:
                    plainText += alphabet[((alphabet.find(letter)) - step) % len(alphabet)]
                else:
                    plainText += letter
        print(len(alphabet) - step)
        print(plainText)
        step -= 1            



deZesar(alphabet_eng, 'VMVIP URP ZJ R EVN TYRETV')
