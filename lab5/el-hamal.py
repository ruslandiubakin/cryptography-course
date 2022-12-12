def isPrimeNumber(number):
    for num in range(2, number):
        if number % num != 0:
            continue
        else:
            return False
    return True


def generate_key(p, g, x):
    if (g < p-1 and x < p-1):
        y = (g ** x) % p
        return y
    else:
        print("Введіть правильні значення!")
        return None


def encrypt(plain_text, g, p, y, k):
    a = (g ** k) % p
    b = ((y ** k) * plain_text) % p
    return [a, b]


def decrypt(cypher_text, p, x):
    return (cypher_text[1] * (cypher_text[0] ** (p - 1 - x))) % p


def main():
    try:
        g = int(input("Введіть просте число g: "))
        p = int(input("Введіть просте число p: "))
        if (not isPrimeNumber(g) or not isPrimeNumber(p)):
            print("Числа не прості!")
            exit()
        x = int(input("Введіть ціле число х: "))
        # k = int(input("Введіть рандомне взаємно просте число з р-1: "))
    except:
        print("Значення не є числом!")

    y = generate_key(p, g, x)
    print(f"Відкритий ключ (p, g, y): ({p, g, y})")
    plain_text = int(input("Введіть текст (число), що потрібно зашифрувати: "))
    k = int(input("Оберіть випадкове ціле число k < p - 1: "))

    cypher_text = encrypt(plain_text, g, p, y, k)
    print(f"Зашифроване повідомлення: {cypher_text}")
    print(f"Розшифроване повідомлення: {decrypt(cypher_text, p, x)}")


main()
print(encrypt(702, 3, 4211, 2395, 3208))
print(encrypt(702, 3, 4211, 2395, 1057))
