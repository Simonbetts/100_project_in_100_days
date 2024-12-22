# 
#
#
#

"""


"""

from cryptography.fernet import Fernet

key_file = open("enc_key.txt", "r")
key = key_file.read()
#fernet = Fernet(str(key))
fernet = Fernet(b'AdexE0gI0reKOBmb0CA2FruKNQNXHOvW9_RHoEhFDq8=')

print(f'What is the name of the file you would like to decrypt?')
#file = input()
file = "enc_message.txt"

encmessage = open(str(file), "r")
print(f'Message Opened')
encMessage = encmessage.read()
print(f'{encMessage}')


decMessage = fernet.decrypt(encMessage).decode()

print(f'Message Reads:\n {decmessage}')
print(f'')

#print("Decrypted string: ", decMessage)