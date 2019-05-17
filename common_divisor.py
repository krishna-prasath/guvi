a=input()
b=input()
c=[a[0]]
for i in range(1,len(a)):
    if a[i] not in c:
        c.append(a[i])
    else:
        break
d="".join(c)
le=len(a)//len(d)
le1=len(b)//len(d)
if min(le,le1)<=2:
    print(min(le,le1))
else:
    print(max(le,le1)//2)
