# Coded by SpiderX
import time

n = int(input())

prime = []
max = 500000

for number in range (2, max + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                time.sleep(1)
                break
        else:
            prime.append(number)
            if len(prime) == n:
                print(prime[n-1])
                break
