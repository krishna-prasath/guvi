a,b=map(str,input().split())
z=[]
x,c="",""
if a[0].islower():
    x=x+a[0].upper()
if b[0].islower():
    c=c+b[0].upper()

for i in range(1,len(a)):
    if a[i].isupper() or a[i].islower():
        x=x+a[i].lower()
for i in range(1,len(b)):
    if b[i].isupper() or b[i].islower():
        c=c+b[i].lower()
z.append(x)
z.append(c)
print(*z)
