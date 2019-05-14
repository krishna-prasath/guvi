a=input()
c=0
if a=='1':
    print(1)
else:
    for i in range(len(a)):
        c=c+(int(a[i])**i)
    print(c)
#stupid conditions
