fact = [1]
for i in range(1, 200_001):
    fact.append(fact[-1] * i % MOD)
def comb(n, k):
    if k > n:
        return 0
    else: 
        return fact[n] * pow(fact[n-k] * fact[k], -1, MOD) % MOD