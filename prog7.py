def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

k = int(input("Enter the value of K = "))
num, pos, count = 2, 0, 0

while count < k:
    if is_prime(num):  
        pos += 1       
        if is_prime(pos):  
            print(num)  
            count += 1   
    num += 1