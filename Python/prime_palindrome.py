"""Write a program to determine the biggest prime palindrome under 1000.

Should always print 929
"""

def palindrome(n):
    for i in reversed(xrange(n)):
        if i == int(str(i)[::-1]) and is_prime(i):
            return i

def is_prime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
    print palindrome(1000)