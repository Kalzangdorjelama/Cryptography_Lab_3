import math

def mod_exp(base, exp, mod):
    return pow(base,exp,mod)


def diffle_hellman():
    p = int(input("Enter the prime number(P): "))
    g = int(input("Enter the number smaller than P: "))
    
    a = int(input("Enter the private key for alice (a): "))
    b = int(input("Enter the private key for bob (b): "))
    
    x = mod_exp(g,a,p)
    y = mod_exp(g,b,p)
    
    secret_key_received_alice = mod_exp(y,a,p)
    secret_key_received_bob = mod_exp(x,b,p)
    
    if secret_key_received_alice == secret_key_received_bob:
        print(f"Shared key is: {secret_key_received_alice}")
    else:
        print("Shared key does not match")

diffle_hellman()