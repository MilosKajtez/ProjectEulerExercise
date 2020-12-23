maxNummber = 600851475143
primeFactors = []

def IsPrime(number):
    isPrime = True
    i = number - 1
    while i > 1:
        if((number % i) == 0):
            isPrime = False
            break
        i-=1
    return isPrime

def getNextPrime(number):
    x = number
    while True:
        x += 1
        if(IsPrime(x)):
            return x

curent = maxNummber
curentPrime = 2

while curent != 1:
    if ((curent % curentPrime) == 0):
        primeFactors.append(curentPrime)
        curent = curent / curentPrime
        curentPrime = 2
    curentPrime = getNextPrime(curentPrime)

result = max(primeFactors)
print("Result:", result)
