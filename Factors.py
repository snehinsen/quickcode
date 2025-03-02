number = int(input("Enter a number: "))

factors = {1}

for i in range(1, number):
    if number % i == 0: # is divisible
        factors.add(i)

factors.add(number)
factorList = []
for factor in factors:
    factorList.append(factor)
factorList.sort()

print(*factorList)
