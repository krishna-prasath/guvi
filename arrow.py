z=int(input())
a=list(map(int,input().split()))
z=""
for i in range(-1,-len(a)-1,-1):
    z=z+str(a[i])+'->'
print(z[0:-2])
