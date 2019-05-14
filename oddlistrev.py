a=input()
a=list(a.split(" "))
for i in range(len(a)):
    if i%2==0:
        a[i]=a[i][-1::-1]
print(" ".join(a))
