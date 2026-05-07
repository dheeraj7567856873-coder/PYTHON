number = int(input("enter the number= "))
if number < 2:
    print("not prime number")
else:
    i = 2
    is_prime = True
    while i < number:
        if number % i == 0:
            print("not prime number")
            is_prime = False
            break
        i += 1
    if is_prime:
        print("prime number")
