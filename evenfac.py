a=int(input())
z=[]
for i in range(2,a+1):
    if a%i==0 and i%2==0:
        z.append(i)
print(*z)
