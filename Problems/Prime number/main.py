number = int(input())
if number > 1:
    i = 2
    while i * i <= number:
        if number % i == 0:
            print("This number is not prime")
            exit()
        i += 1
    print("This number is prime")
elif number == 1:
    print('This number is not prime')