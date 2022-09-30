# Coded by SpiderX

def Algorithm(x, y):
    usr1 = map(int, input().split())
    usr1 = list(usr1)
    if len(usr1) > x:
        exit()

    usr2 = map(int, input().split())
    usr2 = list(usr2)
    if len(usr2) > y:
        exit()

    emp = []

    for k in usr1:
        emp.append(k)

    for j in usr2:
        emp.append(j)

    print(*(sorted(set(emp))))


if __name__ == "__main__":
    x, y = map(int, input().split())
    Algorithm(x, y)
