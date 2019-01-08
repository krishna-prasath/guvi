x=int(input())
y=x
a=0
for i in range(len(str(x))):
    r=x%10
    a=a+r**3
    x=x//10
if y==a:
    print("yes")
else:
    print("no")

