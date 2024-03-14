# 带模快速幂
def quick_pow(x, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x % mod
        x = x * x % mod
        n //= 2
    return result

# 模逆元
def mod_inv(x, mod):
    return quick_pow(x, mod - 2, mod)

def prepare_factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[n] = mod_inv(fact[n], mod)
    for i in range(n, 1, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod
    return fact, inv_fact

def combination(n, m, mod):
    if m < 0 or m > n:
        return 0
    fact, inv_fact = prepare_factorials(n, mod)
    return fact[n] * inv_fact[m] % mod * inv_fact[n - m] % mod

# Example usage:
mod = 10**9 + 7  # A large prime, often used in competitive programming
n, m = 1000000, 500000  # Large values of n and m
print(combination(n, m, mod))