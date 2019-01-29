a1=input()
c,c1=0,0
for i in a1:
	if i.isnumeric():
		c=c+1
	elif i.isalpha():
		c1=c1+1
if c1>0 and c>0:
	print("Yes")
else:
	print("No")
