n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<=j<=k:
                x.append(p*a[i]+q*a[j]+r*a[k])
print(max(x))
