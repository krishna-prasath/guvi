a=input()
z=""
for i in a:
    if i.isupper():
        z=z+i.lower()
    else:
        z=z+i.upper()
print(z)
