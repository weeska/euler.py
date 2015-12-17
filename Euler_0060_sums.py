from stuff.primes import prime_sieve, is_prime_naive
import itertools

primes = list(prime_sieve(1000))
num_primes = len(primes)

def are_quite_remarkable(nums):
    for x, y in itertools.product(nums, nums):
        if x == y:
            continue

        pq = int("".join([str(x), str(y)]))
        if not is_prime_naive(pq):
            return False

    return True

def result():
    for sum_to_check in range(0, 1000):
        for a in range(num_primes):
            aP = primes[a]
            if sum_to_check < aP:
                break
            for b in range(a + 1, num_primes):
                bP = primes[b]
                if sum_to_check < aP + bP:
                    break
                for c in range(b + 1, num_primes):
                    cP = primes[c]
                    if sum_to_check < aP + bP + cP:
                        break
                    for d in range(c + 1, num_primes):
                        dP = primes[d]
                        if sum_to_check < aP + bP + cP + dP:
                            break

                        if are_quite_remarkable([aP,bP,cP,dP]):
                                return sum_to_check

print(result())

