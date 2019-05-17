n,k=map(int,input().split())
a=[]
temp=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    a[i].sort()
for k1 in range(n+k):
    for i in range(k):
        for j in range(n-1):
            if a[j][i]>a[j+1][i]:
                temp=a[j][i]
                a[j][i]=a[j+1][i]
                a[j+1][i]=temp
for i in range(n):
    print(*a[i])
