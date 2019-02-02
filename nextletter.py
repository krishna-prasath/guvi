a=input()
a1=""
for i in a:
    if ord(i)+1>90:
        a1=a1+chr(((ord(i)+1)//26)+64)
    else:
        a1=a1+chr(ord(i)+1)
print(a1)
