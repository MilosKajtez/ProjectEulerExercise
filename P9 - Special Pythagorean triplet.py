#brute force
x = 1000

found = False

for a in range(1, int(x/3)): # if a > x/3 then a<b<c can't be true as a+b+c=1000
    for b in range(a, x-a):  # start from a as a<b | if b > x-a a+b+c can't be 1000
        c = x-a-b
        if(a*a + b*b == c*c):
            found = True
            break
    if(found):
        break

print(a,b,c)

