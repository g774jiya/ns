import hashlib
# Prompt the user to input a message to hash
message = input("Enter a message to hash: ")
# Create a SHA-1 hash object
sha1_hash = hashlib.sha1()
# Update the hash object with the message
sha1_hash.update(message.encode())
# Get the digest of the hash object (i.e., the hashed message)
hashed_message = sha1_hash.digest()
# Print the hashed message in hexadecimal format
print("Hashed message (hex): ", hashed_message.hex())

# Prompt the user to input a modified message
modified_message = input("Enter a modified message to compare: ")

# Create a new SHA-1 hash object
modified_sha1_hash = hashlib.sha1()

# Update the hash object with the modified message
modified_sha1_hash.update(modified_message.encode())

# Get the digest of the hash object (i.e., the hashed modified message)
modified_hashed_message = modified_sha1_hash.digest()

# Compare the original and modified hashed messages
if hashed_message == modified_hashed_message:
    print("The messages are the same.")
else:
    print("The messages are different.")
