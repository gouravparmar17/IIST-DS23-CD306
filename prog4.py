# 1. Write a program in Python that takes an integer k as input and prints all prime numbers till k.


k = int(input("ENter a number : "))

for num in range(2, k + 1):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime: 
        print(num, end = "  ")



