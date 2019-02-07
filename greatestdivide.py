a,b=map(int,input().split())
z=[]
if a==1 and b==1:
    print(1)
else:
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            z.append(i)
    print(max(z))

