k=int(input())
z,x=[],[]
for i in range(k):
    z.append(list(map(int,input().split())))
for i in range(len(z)):
    x=x+z[i]
x.sort()
print(*x)

   #missed my star
