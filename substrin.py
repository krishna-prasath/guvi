a=input()
s=[]
for i in a:
    if i not in s:
        s.append(i)
    else:
        break
print(len(s))
