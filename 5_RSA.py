import math

def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def rsa():
    p = int(input("Enter the prime number (P): "))
    q = int(input("Enter another prime number (Q): "))
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    d = mod_inverse(e, phi)

    msg = 4
    print("Message data =", msg)

    # Encryption c = (msg ^ e) % n
    c = pow(msg, e, n)
    print("Encrypted data =", c)

    # Decryption m = (c ^ d) % n
    m = pow(c, d, n)
    print("Original Message Sent =", m)

rsa()