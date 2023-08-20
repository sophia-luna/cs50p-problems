from PIL import Image, ImageOps
import sys

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".jpeg") and not sys.argv[1].endswith(".png"):
    sys.exit("Not an image.")
pre,suf=sys.argv[1].split(".")
if not sys.argv[2].endswith(suf):
    sys.exit("Output file with a different extension than input file.")

#open shirt
shirt = Image.open("shirt.png")

#open muppet
try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist.")

#get the shirt size as a tuple
size=shirt.size
#create new image the size of the shirt
newimg=ImageOps.fit(img,size)
#overlay shirt on top of image
newimg.paste(shirt, shirt)
#save the muppet
newimg.save(sys.argv[2])