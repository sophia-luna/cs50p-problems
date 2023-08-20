import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

n=0
try:
    with open(sys.argv[1]) as file:
        for lines in file:
            s=lines.strip()
            if s!="" and not s.startswith("#"):
                n+=1
except FileNotFoundError:
    print("File does not exist")
else:
    print(n)