rowCount, colCount, patch = int(input()), int(input()), []
collected = ""

def render():
    for row in patch:
        print(*row, sep="|")

for row in range(rowCount):
    rowInput = input()
    column = []
    for col in range(colCount):
        column.append(rowInput[col])
    patch.append(column)

usedSegments = patch.copy()

x_start, y_start = int(input()), int(input())

def collect_vert(x, y):
    global collected
    # Up
    for i in range(x, -1, - 1):
        if patch[i][y] != "*":
            if usedSegments[i][y] != "U":
                collected += patch[i][y]
                usedSegments[i][y] = "U"
                collect_horz(i, y)
            else:
                continue
        else:
            break
    # down
    for i in range(x,len(patch)):
        if patch[i][y] != "*":
            if usedSegments[i][y] != "U":
                collected += patch[i][y]
                usedSegments[i][y] = "U"
                collect_horz(i, y)
            else:
                continue
        else:
            break

def collect_horz(x, y):
    global collected
    # left
    for i in range(y, -1, - 1):
        if patch[x][i] != "*":
            if usedSegments[x][i] != "U":
                collected += patch[x][i]
                usedSegments[x][i] = "U"
                collect_vert(x, i)
            else:
                continue
        else:
            break

    # Right
    for i in range(y, len(patch[x])):
        if patch[x][i] != "*":
            if usedSegments[x][i] != "U":
                collected += patch[x][i]
                usedSegments[x][i] = "U"
                collect_vert(x, i)
            else:
                continue
        else:
            break

def start():
    collect_vert(x_start, y_start)
    collect_horz(x_start, y_start)

start()
total = collected.count("S") + collected.count("M") * 5 + collected.count("L") * 10

# render()
print(total)
