#justified text

a = "january february march april may june july august september october november december"
z = len(a) - 1
for i in range(-1, z):
    len_detector = len(a[0:])
    i = i + 1
    if len_detector >= 9:
        replacing = a[int(i)].replace(a[i], "#bigword")
        print(replacing)
    else:
        break
