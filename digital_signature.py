import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA

# Generate RSA keys
key = RSA.generate(2048)
private_key = key.exportKey()
public_key = key.publickey().exportKey()

# Prompt the user to input a message to sign
message = input("Enter a message to sign: ")

# Hash the message using SHA-1
hashed_message = hashlib.sha1(message.encode()).digest()

# Sign the hashed message using the private key
signer = pkcs1_15.new(key)
signature = signer.sign(SHA.new(hashed_message))

# Print the signature in hexadecimal format
print("Signature (hex): ", signature.hex())

# Prompt the user to input a message to verify
verified_message = input("Enter a message to verify: ")

# Hash the verified message using SHA-1
hashed_verified_message = hashlib.sha1(verified_message.encode()).digest()

# Verify the signature using the public key
verifier = pkcs1_15.new(key.publickey())
try:
    verifier.verify(SHA.new(hashed_verified_message), signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is invalid.")
