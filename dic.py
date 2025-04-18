def prime_or_not():
    while True:
        number = int(input("Please enter the number you want to check for prime: "))

        if number <= 1:
            print(f"The number {number} is not prime")
            return

        for x in range(2, number):  # Loop through numbers from 2 to number - 1
            if number % x == 0:  # If divisible, it's not a prime number
                print(f"The number {number} is not prime")
                return  # Exit the function once we find a divisor

        print(f"The number {number} is prime")  # If no divisors found, it's prime


prime_or_not()
