s=input("Greeting: ").strip()
s=s.lower()
index=s.find("hello")
if index==0:
    print("$0")
else:
    index=s.find("h")
    if index==0:
        print("$20")
    else:
        print("$100")
