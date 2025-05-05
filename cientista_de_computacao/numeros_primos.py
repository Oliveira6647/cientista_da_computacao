# # def is_prime(n):
# #     for i in range(2, n):
# #         if n % i == 0:
# #             return False
# #     return True
#
#
# print(is_prime(2))

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) +  1):
        if n % i == 0:
            return False
    return True


def find_primes(n):
    return  [i for i in range(2, n) if is_prime(i)]


print(is_prime(2))