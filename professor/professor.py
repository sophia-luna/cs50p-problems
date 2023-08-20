import random

def main():
    level=get_level()
    score=0
    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        j=1
        while True:
            try:
                z=int(input(f"{x} + {y} = "))
            except ValueError:
                if j==3:
                    print(f"{x} + {y} = {x+y}")
                    break
                print("EEE")
                j+=1
            else:
                if z==x+y:
                    score+=1
                    break
                if j==3:
                    print(f"{x} + {y} = {x+y}")
                    break
                print("EEE")
                j+=1
    print("Score:", score)

def get_level():
    while True:
        try:
            level=int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0<level<4:
                return level

def generate_integer(level):
    if level==1:
        start=0
    else:
        start=10**(level-1)
    end=10**level-1
    print(start, end)
    return random.randint(start,end)


if __name__ == "__main__":
    main()