n = input("")
for i in n:n=n.replace("()", "").replace("{}","").replace("[]","")
print(len(n)and"No"or"Yes")