def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input("ENTER A NUMBER..."))

if is_prime(a):
    if 10 <= a < 100:
        print("number is a double digit prime number")
    elif a < 10:
        print("number is a single digit prime number")
else:
    print("not a prime number")