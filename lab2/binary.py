#-*- coding: utf-8 -*-
import random

ENCODING = 'cp866'

def convert_to_bin(line):
    return ' '.join(format(x, "08b") for x in line)

message = 'ok google'
print('Message:    ', message)

message_b = message.encode(ENCODING)



random.seed(7)
key_gamma_b = bytes(random.randint(0, 255) for i in range(len(message_b)))
print('Key gamma:  ', ' '.join(format(x, "03d") for x in key_gamma_b))



print(f'Message b:   {convert_to_bin(message_b)}')

print(f'Key gamma b: {convert_to_bin(key_gamma_b)}')

encoded_b = bytes(x ^ y for x, y in zip(message_b, key_gamma_b))
print(f'Ciphertext:  {convert_to_bin(encoded_b)}')