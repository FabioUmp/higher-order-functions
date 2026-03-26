def get_long_strings(strings):
    
    long_strings = filter(lambda x: len(x) > 5, strings)
    
    return list(long_strings)

def get_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_numbers = filter(is_prime, numbers)
    return list(prime_numbers)