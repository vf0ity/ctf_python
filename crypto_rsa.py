# RSA Cryptography Solving Scripts

## Introduction
This module contains various scripts and functions for breaking weak RSA parameters and performing decryption.

## Functions

### 1. GCD Function
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### 2. Modular Inverse
```python
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1
```

### 3. RSA Decryption Function
```python
def rsa_decrypt(c, n, d):
    """Decrypts a ciphertext 'c' with the private key (n, d)"""
    return pow(c, d, n)
```

### 4. Function to factor n if weak parameters are detected
```python
def factor_n(n):
    # Attempt to factor n (the modulus) if it is weak (not a strong prime)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None
```

### Usage
```python
if __name__ == '__main__':
    # Example usage of the functions
    n = 33  # A weak modulus (3 * 11)
    e = 3   # Public exponent
    c = 27  # Ciphertext to decrypt
    weak_factors = factor_n(n)
    if weak_factors:
        p, q = weak_factors
        d = mod_inverse(e, (p - 1) * (q - 1))  # Calculate private key
        plaintext = rsa_decrypt(c, n, d)
        print(f'Decrypted plaintext: {plaintext}')
```
