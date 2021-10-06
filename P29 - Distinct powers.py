import math

# Define array for A And B where 2<=a<=100 and 2<=b<=100
Aarray = range(2,101)
Barray = range(2,101)

allSqares = []

# Add all squares a pow b to a list
for a in Aarray:
    for b in Barray:
        allSqares.append(pow(a,b))

# Take and count only unique members
distinct = list(set(allSqares))
count = len(distinct)
print(count)