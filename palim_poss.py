a=input()
z=list(a)
temp,c="",0
if a==a[-1::-1]:
    print("YES")
else:
    for i in range(len(a)):
        temp=z[i]
        z[i]=""
        if "".join(z)=="".join(z[-1::-1]):
            c=c+1
        z[i]=temp
    if c>=1:
        print("YES")
    else:
        print("NO")
        
            
