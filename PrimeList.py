def prime(number):
    isPrime = False
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break
        else:
            isPrime = True
    return isPrime

numberStart = int(input("Start: "))
numberEnd = int(input("End: "))

primeNumbers = []

for number in range(numberStart, numberEnd + 1):
    if prime(int(number)):
        primeNumbers.append(number)

print(*primeNumbers)

