a=int(input())
b=list(map(str,input().split()))
b.sort(reverse=True)
print(int("".join(b)))
