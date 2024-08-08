fact = [1]
for i in range(1, 200_001):
    fact.append(fact[-1] * i % MOD)