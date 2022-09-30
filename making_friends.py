# Coded by SpiderX

byang_roll = int(input())

count = 0

for i in range(1, byang_roll):
    if byang_roll % i == 0:
        count += 1

    else:
        i += 1

print(count)
