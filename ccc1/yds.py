size = int(input())

yobis =  []

yobi = int(input())

while yobi != 0:
    yobis.append(yobi)
    yobi = int(input())

for yobiSize in yobis:
    if size > yobiSize:
        size += yobiSize
    else:
        break

print(size)