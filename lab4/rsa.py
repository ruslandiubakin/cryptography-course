import math
import re


def bothsimpl(fn):
    x = 0
    while x != 1:
        y = int(input("Введіть значення експоненти: "))
        if math.gcd(y, fn) == 1:
            x = 1
        else:
            print("Число не взаємно просте з F(n)")
    return y


def generate_keys(p, q):
    n = p * q
    fn = (p-1)*(q-1)
    e = bothsimpl(fn)
    for i in range(0, 10000000):
        if ((e*i) % fn) == 1:
            print("d = ", i)
            d = i
            break
    return [fn, (d, n), (e, n)]


def encrypt(public_key):
    e, n = public_key
    encrypt_values = []
    print("Введіть текст, що потрібно зашифрувати:")
    text_message = input()
    # ascii_values = [ord(character) for character in text_message]
    ascii_values = [int(text_message)]
    print(ascii_values)
    encrypt_ascii_values = [(ascii_values[i]**e) %
                            n for i in range(0, len(ascii_values))]
    print(encrypt_ascii_values)
    # --------------------------------------
    # encrypt_values = [chr(encrypt_ascii_values[i])
    #                   for i in range(0, len(encrypt_ascii_values))]
    # print("".join(encrypt_values))
    # --------------------------------------
    return encrypt_ascii_values


def decrypt(private_key):
    d, n = private_key
    decrypt_values = []
    print("Введіть текст, що потрібно розшифрувати:")
    encrypt_message = input()
    ascii_values = list(
        map(lambda x: int(x), re.findall("\d{1,10}", encrypt_message)))
    decrypt_ascii_values = [(ascii_values[i]**d) %
                            n for i in range(0, len(ascii_values))]
    print(decrypt_ascii_values)
    decrypt_values = [chr(decrypt_ascii_values[i])
                      for i in range(0, len(decrypt_ascii_values))]
    print("".join(decrypt_values))
    return decrypt_ascii_values


def main():
    p = int(input("Введіть просте число p: "))
    q = int(input("Введіть просте число q: "))
    fn, private_key, public_key = generate_keys(p, q)
    print("----------------------------------------------------")
    print("p = ", p)
    print("q = ", q)
    print("n = ", private_key[1])
    print("f(n) = ", fn)
    print("e = ", public_key[0])
    print("d = ", private_key[0])
    print("Приватний ключ: ", private_key)
    print("Публічний ключ: ", public_key)
    print("----------------------------------------------------")
    print("Що потрібно зробити?")
    print("1. Зашифрувати")
    print("2. Розшифрувати")
    menu_value = input()
    if menu_value == '1':
        encrypt(public_key)
    elif menu_value == '2':
        decrypt(private_key)


main()
