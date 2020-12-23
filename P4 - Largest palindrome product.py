#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

# Check if number is palindrome
def  isPalindrome(number):
    strValue = str(number)
    i = 0
    ii = len(strValue) -1
    while ii > i:
        if (strValue[i] != strValue[ii]):
            return False
        ii -=1
        i += 1
    return True

# Gets largest palindrom for 3 digits products
def getLargestPalindrome():
    i = 999
    ii = 999

    palindroms =[]

    # Add largest plaindrom for each of outer loop numbers.
    # First palindrom found it's not largest 
    # first 995 * 583 = 580085
    # largest 993 * 913 = 906609
    while i > 99:
        while ii > 99:
            x = i*ii
            if(isPalindrome(x)):
                palindroms.append(x)
                break
            ii -=1
        i-= 1
        ii = i
    
    return max(palindroms)

result = getLargestPalindrome()

print(result)
