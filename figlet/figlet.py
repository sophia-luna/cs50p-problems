from pyfiglet import Figlet
import sys

figlet=Figlet()
if len(sys.argv)!=1 and len(sys.argv)!=3:
    sys.exit("wrong amount of arguments")
if len(sys.argv)==3:
    if sys.argv[1]!='-f' and sys.argv[1]!='--font':
        sys.exit("fisrt argument not accepted")

    fonts=figlet.getFonts()
    if sys.argv[2] not in fonts:
        sys.exit("second argument not accepted")

    figlet.setFont(font=sys.argv[2])

s=input("Input: ")
print("Output: ")
print(figlet.renderText(s))