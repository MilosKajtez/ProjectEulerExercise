#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

# Check if number is prime number
def IsPrime(number):
    i =2
    while i < number:
        # If number is devidable( modulo is 0)  it's not prime
        if((number % i) == 0):
            return False
        i+=1
    return True

# Get next prime number
def getNextPrime(number):
    x = number
    while True:
        x += 1
        if(IsPrime(x)):
            return x

primes = []
x = 1
count = 0

while count < 10001:
    next = getNextPrime(x)
    primes.append(next)
    x = next
    count += 1
    print(count)
    print(x)

print(x)