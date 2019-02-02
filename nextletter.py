a=input()
a1=""
for i in a:
    if ord(i)+3>90:
        a1=a1+chr(((ord(i)+3)//26)+64)
    else:
        a1=a1+chr(ord(i)+3)
print(a1)
#misjudged the values
