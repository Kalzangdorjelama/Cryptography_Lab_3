def gcd(a, b):
   
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    
    result = n   # Initialize result as n

    # Check each number from 2 to n
    for p in range(2, n + 1):
        # If p is a divisor of n
        if n % p == 0:
            # Check if p is a prime factor
            while n % p == 0:
                n //= p
            result -= result // p
    
    return result

def main():
    n = int(input("Enter a number: "))
    print(f"Euler's Totient Function φ({n}) = {euler_totient(n)}")

if __name__ == "__main__":
    main()