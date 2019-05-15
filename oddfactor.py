a=int(input())
z=[]
if a==1:
    print(1)
else:
    for i in range(1,a+1):
        if a%i==0 and i%2!=0:
            z.append(i)                       #hope this works
    print(*z)
