s=input("camelCase: ")
a=""
for i in range(len(s)):
    if s[i].isupper():
        a=a+'_'+s[i].lower()
    else:
        a+=s[i]
print(f"snake_case: {a}")