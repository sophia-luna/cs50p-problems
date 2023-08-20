s=input("What is the answer to the Great Question of Life, the Universe and Everything? ")
s=s.lower()
if s=="forty two" or s=="forty-two":
    print("Yes")
else:
    s=s.replace(' ','')
    if s=="42":
        print("Yes")
    else:
        print("No")