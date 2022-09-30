# Coded by SpiderX

for i in range(4):
    if i == 0:
        a11, a12 = map(int, input().split())

    elif i == 1:
        a21, a22 = map(int, input().split())

    elif i == 2:
        b11, b12 = map(int, input().split())

    elif i == 3:
        b21, b22 = map(int, input().split())

    else:
        pass

print(((a11*b11)+(a12*b21)), ((a11*b12)+(a12*b22)))
print(((a21*b11)+(a22*b21)), ((a21*b12)+(a22*b22)))
