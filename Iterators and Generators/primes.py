from math import sqrt


def is_price(value):
    for x in range(2, int(sqrt(value) + 1)):
        if value % 2 == 0:
            return False
    return True


class Primes:
    def __init__(self, max_value):
        self.max_value = max_value
        self.last_pripe = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_prime = self.last_pripe + 1
        while current_prime <= self.max_value and not is_price(current_prime):
            current_prime += 1

        if current_prime > self.max_value:
            raise StopIteration
        self.last_pripe = current_prime
        return current_prime


primes = Primes(12)

[print(x) for x in primes]
