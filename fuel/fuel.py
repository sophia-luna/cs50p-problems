while True:
    s=input("Fraction: ")
    try:
        x,y=s.split("/")
        x=int(x)
        y=int(y)
        z=x/y
    except (ValueError,ZeroDivisionError):
        pass
    else:
        z*=100
        z=round(z)
        z=int(z)
        if z>=0 and z<=100:
            break

if z<=1:
    print("E")
elif z>=99:
    print("F")
else:
    print(z,"%",sep='')