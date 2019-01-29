a1,a2=map(int,input().split())
c=0
a3=list(map(int,input().split()))
for i in a3:
	if i==a2:
		c=c+1
print(c)
