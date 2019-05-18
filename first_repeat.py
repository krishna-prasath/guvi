a=int(input())
x=list(map(int,input().split()))
z=[x[0]]
for i in range(1,a):
    if x[i] in z:
        print(x[i])
        break
    else:
        z.append(x[i])
