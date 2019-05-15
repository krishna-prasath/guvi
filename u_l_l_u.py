a=input()
z=""
for i in a:                         #if everyone does the same logic what should i do
    if i.isupper():
        z=z+i.lower()
    else:
        z=z+i.upper()
print(z)
