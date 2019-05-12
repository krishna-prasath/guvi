a=input()
z=0
for i in range(len(a)):
    z=z+int(a[i])
z=str(z)
if z==z[-1::-1]:
    print("YES")
else:
    print("NO")
    

