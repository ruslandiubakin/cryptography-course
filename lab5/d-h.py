
def isPrimeNumber(number):
    for num in range(2, number):
        if number % num != 0:
            continue
        else:
            return False
    return True


def publicKeyDiffiHellman(g, p, private_key):
    public_key = (g ** private_key) % p
    return public_key


def commonKeyDiffiHellman(p, private_key, public_key):
    common_key = (public_key ** private_key) % p
    return common_key


def main():
    try:
        g = int(input("Введіть просте число g: "))
        p = int(input("Введіть просте число p: "))
        if (not isPrimeNumber(g) or not isPrimeNumber(p)):
            print("Числа не прості!")
            exit()
        a = int(input("Введіть секретний ключ Аліси: "))
        b = int(input("Введіть секретний ключ Боба: "))
    except:
        print("Значення не є числом!")

    A = publicKeyDiffiHellman(g, p, a)
    print("Публічний ключ Аліси: ", A)

    B = publicKeyDiffiHellman(g, p, b)
    print("Публічний ключ Боба", B)

    print("Обмін публічними ключами...")

    Ka = commonKeyDiffiHellman(p, a, B)
    print("Ключ К у Аліси: ", Ka)

    Kb = commonKeyDiffiHellman(p, b, A)
    print("Ключ К у Боба: ", Kb)


main()
