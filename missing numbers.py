#thought game

import math

r = int(input())

a, b = list(map(int, input().split()))[:r]

z = (a + b) % 2

d = math.floor(z)

if d == 0:
    print("Oops!")

else:
    print("Sadia will be happy.")

