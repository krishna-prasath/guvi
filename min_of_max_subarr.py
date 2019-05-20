n,k=map(int,input().split())
li=list(map(int,input().split()))
a,f=[],[]
for i in range(n):
    a.append(list(li[i:k+i]))
for i in range(len(a)):
    f.append(min(a[i]))
print(max(f))          #dscsvs
