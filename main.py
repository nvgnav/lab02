def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []  # Handle cases where limit is less than 2
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, limit + 1, i):
                primes[multiple] = False

    return [p for p, is_prime in enumerate(primes) if is_prime]

if __name__ == "__main__":
    try:
        limit = int(input("Enter the limit: "))
        if limit < 2:
            print("Limit must be at least 2.")
        else:
            primes = sieve_of_eratosthenes(limit)
            print("Prime numbers up to", limit, "are:", primes)
    except ValueError:
        print("Invalid input. Please enter an integer.")