a=int(input())
x=list(map(int,input().split()))
z,c=[x[0]],0
for i in range(1,a):
    if x[i] in z:
        c=x[i]        
        break
    else:
        z.append(x[i])
if c!=0:
    print(c)
else:                               # slight changes for Unique
    print("unique")
