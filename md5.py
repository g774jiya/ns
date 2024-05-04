import hashlib

# Prompt the user to input a message to hash
message = input("Enter a message to hash: ")

# Create an MD5 hash object
md5_hash = hashlib.md5()

# Update the hash object with the message
md5_hash.update(message.encode())

# Get the digest of the hash object (i.e., the hashed message)
hashed_message = md5_hash.digest()

# Print the hashed message in hexadecimal format
print("Hashed message (hex): ", hashed_message.hex())
