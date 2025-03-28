
#Домашнее задание №1

def power_numbers(*args):
    return [number ** 2 for number in args]

result = power_numbers(1, 2, 3, 4, 5, 6, 7, 8)
print(result)


#Домашнее задание №2

ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))

print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 22, 27, 29], ODD))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 22, 27, 28], EVEN))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 23, 27, 29], PRIME))
