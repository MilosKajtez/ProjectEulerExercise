#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

maxNumber = 600851475143
primeFactors = []

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

curent = maxNumber
curentPrime = 2


while curent != 1:
    # If prime is prime factor devide, add it to list and start from 2
    if ((curent % curentPrime) == 0):
        primeFactors.append(curentPrime)
        curent = curent / curentPrime
        curentPrime = 2
    # If prime is not prime factor, get next prime
    curentPrime = getNextPrime(curentPrime)

# Get biggest prime fator from list
result = max(primeFactors)
print("Result:", result)