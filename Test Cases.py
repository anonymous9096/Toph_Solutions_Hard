
x, y, z = map(int, input().split())

for i in range(x):
    q, w, e = map(int, input().split())
    if w > y:
        print("CLE")
        exit()

    elif e > z:
        print("MLE")
        exit()

    elif q != 0:
        print("WA")
        exit()

    else:
        continue

print("AC")

