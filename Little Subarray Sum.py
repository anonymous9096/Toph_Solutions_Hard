# Coded by SpiderX

n, a, b = map(int, input().split())

z = 0

for i in range(1):
    usr = map(int, input().split())
    usr = list(usr)
    if len(usr) == n:
        for k in range(a, b+1):
            z += usr[k]

print(z)
