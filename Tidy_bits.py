# Coded by Spider

usr = int(input())
emp = list(bin(usr))
final = []

emp.remove('b')

for i in range(len(emp)):
    if emp[i] == '0':
        i += 1

    else:
        final.append(int(emp[i]))

digit = 0

for low in range(len(final)):
    digit += (final[low]*(2**low))

print(digit)
