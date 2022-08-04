#method to encrypt and decrypt file
#first generate key , Write in file , read files in bytes, 
#open file that contains Password, also the file that contatins key , use encryption method
#write the encrypted key (var) in file
from cryptography.fernet import Fernet
#get the key from the file
file = open("KEY.key", "rb")
key = file.read()
file.close()

with open("PW.dll","rb") as f:
    password=f.read()
    f.close()

fernet = Fernet(key)
encrypted = fernet.decrypt(password)
original_pass = encrypted.decode() # this will remove byte
print(original_pass)


