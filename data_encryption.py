from Crypto.Cipher import DES
from base64 import b64encode

# Get the key and the message from the user
key = input("Enter the key (8 characters): ")
message = input("Enter the message: ")

# Convert the key and the message to bytes
key = key.encode('utf-8')
message = message.encode('utf-8')

# Check if the key is 8 bytes long
if len(key) != 8:
    raise ValueError("The key must be 8 bytes long")

# Pad the message to a multiple of 8 bytes
message_length = len(message)
padding_length = 8 - (message_length % 8)
padded_message = message + padding_length * bytes([padding_length])

des_obj = DES.new(key, DES.MODE_ECB)

encrypted_message = des_obj.encrypt(padded_message)

print("Encrypted message:", b64encode(encrypted_message))

decrypted_message = des_obj.decrypt(encrypted_message).rstrip(bytes([padding_length]))

print("Decrypted message:", decrypted_message)
