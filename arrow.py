z=int(input())
a=list(map(int,input().split()))
z=""
a.sort(reverse=True)
for i in a:
    z=z+str(i)+'->'

print(z[0:-2])
