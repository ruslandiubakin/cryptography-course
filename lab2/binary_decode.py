#-*- coding: utf-8 -*-
ENCODING = 'cp866'

gamma_binary = \
    '11000011 01010100 11110001 01101001 10000101 11011010 10001000 01010011 01101000 10111111'
ciphertext_binary = \
    '10001001 00010101 10111111 00101100 11000100 10001111 11011011 00000111 00101101 11110001'

gamma_int = [int(x, 2) for x in gamma_binary.split()]
print("Key_gamma  (int): ", gamma_int)

ciphertext_int = [int(x, 2) for x in ciphertext_binary.split()]
print("Ciphertext (int): ", ciphertext_int)
            
message_b = bytes(x ^ y for x, y in zip(ciphertext_int, gamma_int))
print("Message: ", message_b.decode(ENCODING))
