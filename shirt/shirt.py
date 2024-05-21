import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        if ".jpg" in sys.argv[2] or ".jpeg" in sys.argv[2] or ".png" in sys.argv[2]:
            if (".jpg" in sys.argv[1] and ".jpg" in sys.argv[2]) or (".png" in sys.argv[1] and ".png" in sys.argv[2]) or (".jpeg" in sys.argv[1] and ".jpeg" in sys.argv[2]):
                shirt = Image.open("shirt.png")
                person = Image.open(sys.argv[1]) #https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
                size = shirt.size
                newperson = ImageOps.fit(person, size) #https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
                newperson.paste(shirt,shirt) #https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste
                newperson.save(sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")

    except FileNotFoundError:
        sys.exit("Input does not exist")

