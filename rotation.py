z,n=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    z=a[-1]
    a.remove(a[-1])
    a.insert(0,z)
print(*a)
