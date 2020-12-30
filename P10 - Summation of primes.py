def getsum(x):
    nums = [True] * x
    sum = 0
    for n in range(2,x):
        if nums[n]:
            sum += n
            for m in range(n,x,n):
                nums[m] = False

    return sum

sum = getsum(2000000)
print(sum)