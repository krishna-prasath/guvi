n=int(input())
a=[]
for i in range(n):
    a.append(input())
z=a[0]
x,c=0,0
a1=""
for i in range(len(z)):
    c=0
    for j in range(1,n):
          if z[i]==a[j][i]:
            c=c+1
    if c==n-1:
       a1=a1+z[i]
    else:
        break
print(a1)
