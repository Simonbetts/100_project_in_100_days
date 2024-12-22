# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	21/12/2024

"""
Day 16: Cryptogrphy

"""

from cryptography.fernet import Fernet

# we will be encrypting the below string.
#message = "hello geeks"
message = open("message.txt", "r")
message = message.read()
#message = str(message)
#print(str(message.read()))

# generate a key for encryption and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the Fernet class instance 
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())

print("Original string: ", message)
print(f' ')
print("Encrypted string: ", encMessage)
print(f' ')

# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()

print("Decrypted string: ", decMessage)