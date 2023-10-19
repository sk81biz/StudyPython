def is_prime(num):
    for i in range(2,num):
        print (num%i, end = " ")
        if num%i == 0:
            return False
    return True

test = [5,4,18,13]

print(test)

for num in test:
    print(f"{num} if a prime number {is_prime(num)}")

