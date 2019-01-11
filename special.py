inp=input()
l=len(inp)
for i in inp:
  if i.isdigit() or i.isalpha():
    l=l-1
print(l)
