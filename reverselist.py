a=input()
b=list(a.split())
print(b)
l=[x[::-1] for x in b]
print(*l)
