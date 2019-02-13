a=input()
a=list(a)
z,x=[],[]
for i in range(len(a)):
    z.append(a[i])
for i in range(-1,-len(a)-1,-1):
    x.append(a[i])

if "".join(x)=="".join(z):
    print("YES")
else:
    print("NO")
    
