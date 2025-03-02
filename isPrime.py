number = int(input("Enter a number: "))

isPrime = False

for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break
    else:
        isPrime = True

if isPrime:
    print("Prime")
else:
    print("Not prime")