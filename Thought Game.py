#thought game

cases = int(input(""))

for i in range(cases):
    a1, b1 = map(int, input("").split())

    sum1 = (a1 + b1)//2
    if sum1 % 2 == 0:
        print("Sadia will be happy.")

    else:
        print("Oops!")
