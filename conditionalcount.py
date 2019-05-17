a=int(input())
d=list(map(int,input().split()))
c=0
for i in range(a):
    for j in range(a):
        for k in range(a):
            if d[i]<d[j]<d[k] and i<j<k:
                c=c+1
print(c)
               
