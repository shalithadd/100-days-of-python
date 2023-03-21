def prime_checker(number):
    is_prime = False

    if number < 2:
        is_prime = False
    elif number == 2:
        is_prime = True
    elif number % 2 == 0:
        is_prime = False

    for i in range(3, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Enter a number: "))
prime_checker(n)
