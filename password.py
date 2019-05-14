a,b=map(str,input().split())
z,x,lis,c=a,b,[],0
if len(a)>len(b):
    c=len(a)-len(b)
    for i in range(1,c+1):
        x=x+str(i)
else:
    c=len(b)-len(a)
    for i in range(1,c+1):
        z=z+str(i)
for i in range(len(x)):
    lis.append(z[i])
    lis.append(x[i])
print("".join(lis))
