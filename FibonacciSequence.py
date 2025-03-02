how_many = int(input("How many numbers in the sequence? "))

prev = 0
next = 1

for i in range(how_many):
    print(prev)
    tmp = prev
    prev = next
    next = tmp + prev
