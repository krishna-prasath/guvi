n,d=map(int,input().split())
a=list(map(int,input().split()))
for i in range(d):
    z=a[0]
    a.remove(a[0])
    a.append(z)
print(a)
    
