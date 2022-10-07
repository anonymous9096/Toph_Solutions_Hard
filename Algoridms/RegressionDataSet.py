from turtle import *

print("\n Data-Set algorithm \n")

dataset = []
print(dataset)
while True:
    try:
        usr = int(input("Enter the number :"))
        if 1 <= usr <= 10:
            open('algo.txt', 'w')
            write(usr)

        else:
            print("Enter between 1-10")

    except Exception as e:
        print(e)

