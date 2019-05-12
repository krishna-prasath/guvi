a=input()
a=list(a)
z=[a[0]]
for i in range(1,len(a)):
    if a[i] not in z:
        z.append(a[i])
print("".join(z))

        
