import hashlib

#print(hashlib.algorithms_available, '\n')

#print(hashlib.algorithms_guaranteed, '\n')

#hash_obj = hashlib.sha1(b'Hello, world!')
#print('Hello, world!', hash_obj.hexdigest(), 4*len(hash_obj.hexdigest()))

'''
hash_obj = hashlib.sha1(b'abc')
print(hash_obj.hexdigest(), '\n')

hash_obj = hashlib.sha256(b'abc')
print(hash_obj.hexdigest(), '\n')

hash_obj = hashlib.sha512(b'abc')
print(hash_obj.hexdigest())
'''

hash_obj = hashlib.sha1(b'')
print(hash_obj.hexdigest())
