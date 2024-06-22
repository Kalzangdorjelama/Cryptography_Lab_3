def modular_exponentiation(base, exp, mod):
   
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def miller_rabin_test(n, a):
    
    if n <= 1:
        return 'composite'
    if n <= 3:
        return 'prime'

    
    m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1

  
    t = modular_exponentiation(a, m, n)

    
    if t == 1 or t == n - 1:
        return 'prime'

    for _ in range(k - 1):
        t = (t * t) % n
        if t == n - 1:
            return 'prime'
        if t == 1:
            return 'composite'

    return 'composite'

def main():
    n = int(input("Enter the number to test: "))
    a = int(input("Enter the base: "))

    result = miller_rabin_test(n, a)
    print(f"The number {n} is {result} for base {a}.")

if __name__ == "__main__":
    main()