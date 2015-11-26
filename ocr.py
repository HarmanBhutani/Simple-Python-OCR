# coding=utf-8
from PIL import Image
import pytesseract
import re, os


def image_to_string(filename):
    ret = re.search("\.", filename)
    if ret:
        file = os.path.basename(filename)
        im = Image.open(file)
        im = im.convert("L")
        width = im.size[0]
        height = im.size[1]
        for h in range(0, height):
            for w in range(0, width):
                pixel = im.getpixel((w, h))
                if (pixel >= 140):
                    im.putpixel((w, h), 255)
                else:
                    im.putpixel((w, h), 0)

        box = (1, 1, 99, 34)
        im = im.crop(box)
	#prefix = re.search(r"(\w+)(.+)", file)
	#head = prefix.group(1)
        #im.save(head + ".tif")
        return (pytesseract.image_to_string(im)).replace(' ', '')
    else:
        print "!! no *.jpeg !!"

