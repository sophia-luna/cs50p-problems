from random import randint

while True:
    try:
        level=int(input("Level: "))
    except ValueError:
        pass
    else:
        if level>0:
            break

n=randint(1,level)

while True:
    try:
        guess=int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess==n:
            print("Just right!")
            break
        if guess>n:
            print("Too large!")
        else:
            print("Too small!")