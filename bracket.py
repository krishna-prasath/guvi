a=input()
c,c2=0,0
for i in range(len(a)):
    if a[i]=="(":
        c=c+1
    else:
        c2=c2+1
if c==c2:
    print("yes")
else:
    print("no")
    
