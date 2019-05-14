n,k=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(n):
    if a[i]!=k:
        x.append(a[i])
if len(x)==0:
    print("empty")
else:
    print(*x)
