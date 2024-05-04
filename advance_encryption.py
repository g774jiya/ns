from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = input("Enter the key (16, 24, or 32 characters): ")
message = input("Enter the message: ")

key = key.encode('utf-8')
message = message.encode('utf-8')

iv = get_random_bytes(AES.block_size)

cipher_enc = AES.new(key, AES.MODE_CBC, iv=iv)

padded_message = pad(message, AES.block_size)

encrypted_message = cipher_enc.encrypt(padded_message)

encrypted_message = iv + encrypted_message

print("Encrypted message (hex): ", encrypted_message.hex())

iv = encrypted_message[:AES.block_size]
encrypted_message = encrypted_message[AES.block_size:]
cipher_dec = AES.new(key, AES.MODE_CBC, iv=iv)

decrypted_message = cipher_dec.decrypt(encrypted_message)

decrypted_message = unpad(decrypted_message, AES.block_size)

print("Decrypted message: ", decrypted_message.decode('utf-8'))
