# Define a function to compute the modular exponentiation of a base raised to an exponent modulo a modulus
def modular_exponentiation(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result
# Prompt the user to input two prime numbers
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
# Compute the product of p and q (n = p*q)
n = p * q
# Choose a base g such that 1 < g < n
g = 2
# Choose a private key a such that 1 < a < n
a = int(input("Enter a private key a (1 < a < n): "))
# Compute the public key A = g^a mod n
A = modular_exponentiation(g, a, n)
# Choose a private key b such that 1 < b < n
b = int(input("Enter a private key b (1 < b < n): "))
# Compute the public key B = g^b mod n
B = modular_exponentiation(g, b, n)
# Compute the shared secret S = A^b mod n = B^a mod n
S1 = modular_exponentiation(B, a, n)
S2 = modular_exponentiation(A, b, n)
if S1 != S2:
    print("Error: shared secrets do not match!")
else:
    shared_secret = S1
    print("Shared secret:", shared_secret)
print(f"Public Key generated for user A: {A}")
print(f"Public Key generated for user B: {B}")