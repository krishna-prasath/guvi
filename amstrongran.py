x,y=map(int,input().split())
z=0

for j in range(x,y):
    z=j
    a=0
    for i in range(len(str(j))):
        r=j%10
        a=a+r**3
        j=j//10
    if a==z:
       print(a, end=" ")
print()
#still one test case 
#still asdd
