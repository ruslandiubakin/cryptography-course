

alphabet_eng = "abcdefghijklmnopqrstuvwxyz"

def vigenere(alphabet, plainText, keyword):
    cryptoText = ''
    times = (len(plainText) // len(keyword)) + 1
    keyword = keyword * times
    keyword = keyword[ :(len(plainText) - len(keyword))]
    for letter, keyLetter in zip(plainText.lower(), keyword.lower()):
        if letter in alphabet:
            value = (alphabet.find(letter) + alphabet.find(keyLetter)) % len(alphabet)
            cryptoText += alphabet[value]
        else:
            cryptoText += letter
    print(cryptoText)
    return cryptoText

def deVigenere(alphabet, cryptoText, keyword):
    plainText = ''
    times = (len(cryptoText) // len(keyword)) + 1
    keyword = keyword * times
    keyword = keyword[:(len(cryptoText) - len(keyword))]
    for letter, keyLetter in zip(cryptoText.lower(), keyword.lower()):
        if letter in alphabet:
            value = (alphabet.find(letter) -
                     alphabet.find(keyLetter) + len(alphabet)) % len(alphabet)
            plainText += alphabet[value]
        else:
            plainText += letter
    print(plainText)
    return plainText

vigenere(alphabet_eng, "iloveukraine", "bandera")
deVigenere(alphabet_eng, "jlbyilksavqi", "bandera")
