a=int(input())
b=list(map(int,input().split()))
z=[]
for i in range(a):
    if b[i]==i:
        z.append(b[i])
if len(z)>0:
    print(*z)
else:
    print(-1)
