a=input()
c=0
for i in a:
	if int(i)==0 or int(i)==1:
		c=c+1
if c==len(a):
	print("yes")
else:
	print("no")
