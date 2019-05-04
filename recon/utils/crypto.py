from Crypto.Cipher import AES

def aes_decrypt(ciphertext, key, iv):
    decoded = ciphertext.decode('base64')
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    password = cryptor.decrypt(decoded)
    return str(password, 'utf-8')
