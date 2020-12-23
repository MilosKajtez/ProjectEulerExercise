#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

maxNumber = 4000000

# Two consecutive nummber of array
x = 1
y = 2

# Temp variable used to hold value while we calculate next values in array
tmp = 0

result = 0

while y < maxNumber:
    # If nummber if even (modulo is 0) add it to result
    if (y % 2) == 0:
        result += y
    # Save old bigger value
    tmp = y
    # Calculate next value of array 
    y += x
    # Assign previus value to x to be used in calculation
    x = tmp
    
print("Result:", result)