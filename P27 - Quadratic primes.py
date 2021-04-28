def isPrime(num):
    if(num <= 1):
         return False
    for i in range(2,num):
        if((num % i) == 0): 
            return False
    return True

limit = 1000

count = 0
value_a = 0
value_b = 0

for a in range(-limit, limit):
    for b in range(-limit, limit):
        primes = 0
        while(isPrime(primes * primes + primes * a + b)):
            primes += 1
        
        if(count < primes):
            count = primes
            value_a = a
            value_b = b

product = value_a * value_b
print(product)
