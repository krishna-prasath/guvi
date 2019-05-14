a=input()
if a[-1]==".":
    a=a[:-1]
a=list(a.split(" "))
for i in range(len(a)):
    if i%2==0:
        a[i]=a[i][-1::-1]
print(" ".join(a))
        # wrong test case
