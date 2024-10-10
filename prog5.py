
# 2. Write a program in Python that takes an integer k as input and prints first k prime numbers

k = int(input("Enter a numnber : "))

count, num = 0, 2

while count < k:
    
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime == True:
        print(num, end = "  ")
        count += 1

    num += 1




    
