"""Write a program to determine the sum of the first 1000 prime numbers.

Should always output 3682913
"""

def nprimes(n):
    counter = 0
    current = 2
    prime_sum = 0
    while counter < n:
        if is_prime(current):
            prime_sum += current
            counter += 1
        current += 1
    return prime_sum

def is_prime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
        else:
            pass
    return True


if __name__ == '__main__':
    print nprimes(1000)
