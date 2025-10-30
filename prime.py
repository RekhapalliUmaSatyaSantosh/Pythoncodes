# num=int(input("Enter a number:"))
# i=2
# if num%i == 0:
#     print("Not a prime number")
# else:
#     print("Prime number")

num = int(input("Enter the range:"))
if num < 2:
    print("There are no prime numbers in this range.")
else:
    primes = []
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    print("Prime numbers in the range:", primes)