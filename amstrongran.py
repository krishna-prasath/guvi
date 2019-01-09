x,y=map(int,input().split())
z=0
c=[]
for j in range(x,y):
    z=j
    a=0
    for i in range(len(str(j))):
        r=j%10
        a=a+r**3
        j=j//10
    if a==z:
      c.append(a)
print(*z)
#still one test case 
#changes done bro....
