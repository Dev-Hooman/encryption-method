from cryptography.fernet import Fernet


#this file is created from Key Generator, we use same key with encryption and decryption
with open("KEY.key","rb") as f:
    key=f.read()
    f.close()
    
    
message = "anyPassword"
encoded = message.encode();

f= Fernet(key)
encrypted  = f.encrypt(encoded)
print (encrypted)


filepw = open("PW.dll","wb")  #TypeError: write() argument must be str, not bytes if "w" only
filepw.write(encrypted)
filepw.close()