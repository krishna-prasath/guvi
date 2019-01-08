a,b=map(int,input().split())
z=[]
for i in range(a+1,b):
    if i%2==0:
        z.append(i)
print(*z)
#made some small changes lol
