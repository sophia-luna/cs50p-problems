names=[]
n=0
while True:
    try:
        names.insert(n,input("Name: ").strip())
        n+=1
    except EOFError:
        break

print("Adieu, adieu, to ", end='')
for i in range(n):
    print(names[i], end='')
    if n==2 and i==0:
        print(" and ", end='')
    else:
        if i<n-2:
            print(', ', end='')
        elif i==n-2:
            print(", and ", end='')

print()