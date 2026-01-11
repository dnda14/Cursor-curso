# funcion para determinar si un numero es primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(11))
print(is_prime(12))
print(is_prime(13))
print(is_prime(14))
print(is_prime(15))