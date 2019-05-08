a=input()
z=""
w=['a','e','i','o','u']
for i in a:
    if i in w:
        z=z+i
for i in a:
    if i not in w:
        z=z+i
print(z)
