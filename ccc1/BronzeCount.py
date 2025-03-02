from itertools import count

players = int(input())

scores = []
for i in range(players):
    scores.append(int(input()))

gold = 0
silver = 0
bronze = 0

for score in scores:
    if score > gold:
        gold = score

for score in scores:
    if silver < score < gold:
        silver = score


for score in scores:
    if bronze < score < silver:
        bronze = score

print(bronze, scores.count(bronze))