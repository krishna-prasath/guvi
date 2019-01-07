n=input()
if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
  print("Vowel")
elif str(type(n))== "<class 'str'>":
  print("Consonant")
else:
  print("invalid")
