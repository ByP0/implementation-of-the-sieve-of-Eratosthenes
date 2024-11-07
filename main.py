def get_primes(n):
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
        for i in range(p * p, n, p):
            sieve[i] = False
    return primes

if __name__ == "__main__":
    while True:
        try:
            max_value = int(input("Введите целое число до которого будем искать: "))
            print(get_primes(max_value))
        except ValueError:
            print("Введите целое число!\n")