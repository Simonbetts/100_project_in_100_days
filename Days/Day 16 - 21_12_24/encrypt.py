# 
#
#
#

"""


"""

from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

key_file = open("enc_key.txt", "w")
key_file.write(str(key))
key_file.close()

print(f'What is the name of the file you would like to encrypt?')
#file = input()
file = "message.txt"

message = open(str(file), "r")
message = message.read()


print(f'Original string:\n {message}')
print(f' ')

encMessage = fernet.encrypt(message.encode())
print(f'## Message Enrypted ##')
print(f' ')

end_file = open("enc_message.txt", "w")
end_file.write(str(encMessage))
end_file.close()

