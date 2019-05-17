a,k=map(int,input().split())
d=list(map(int,input().split()))
for i in range(k-1):
    d.remove(min(d))
print(min(d))
