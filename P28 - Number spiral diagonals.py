# Difference in nummbers on diagonal is a even number that increas every circle 2,4,6..
# For 1001 x 1001 we have 500 "circles" for each circle 4 numbers 
# eg:
#789
#612
#543
# First "circle" is 3,5,7,9

current = 1
nums = [2]
lastIndex = 0

#get even numbers
while(len(nums) < 500):
    nums.append(nums[lastIndex]+2)
    lastIndex += 1

diagonalNums = [1]

# For each circle add 4 numbers
for i in nums:
    current += i
    diagonalNums.append(current)
    current += i
    diagonalNums.append(current)
    current += i
    diagonalNums.append(current)
    current += i
    diagonalNums.append(current)

# get sum
print(sum(diagonalNums))